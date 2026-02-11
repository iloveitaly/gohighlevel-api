# Set up the Python environment
setup:
    uv venv && uv sync
    @echo "activate: source ./.venv/bin/activate"

# Run tests
test:
    uv run pytest -v

# python linting checks
[script]
lint FILES=".":
    uv run ruff check {{FILES}}
    uv run ruff format --check {{FILES}}
    uv run pyright {{FILES}}

# Automatically fix linting errors
lint-fix:
    uv run ruff check . --fix
    uv run ruff format .

# Clean build artifacts
clean:
    rm -rf *.egg-info .venv || true
    find . -type f -name "*.pyc" -delete
    find . -type d -name "__pycache__" -delete || true

# Download and merge schemas
download_merge_schemas:
    uv run python scripts/merge_schemas.py

# Generate client
generate: download_merge_schemas
    mkdir -p build
    rm -rf build/gen
    uvx openapi-python-client@latest generate \
        --path ./ghl_schema/combined.yaml \
        --meta uv \
        --config openapi-config.yaml \
        --output-path build/gen \
        --overwrite
    rm -rf ghl_client
    cp -r build/gen/gohighlevel_api .
    cp build/gen/pyproject.toml .
    cp build/gen/README.md .
    rm -rf build/gen
    # Re-sync to install new dependencies if any
    uv sync
    # Re-add dev dependencies
    uv add --dev ruff pyright pytest jsonpath-ng pyyaml

# Build package
build:
    uv build

# Publish package
publish:
    uv publish

# set publish permissions, update metadata, and protect master; all in one command
github_setup: github_repo_permissions_create github_repo_set_metadata github_ruleset_protect_master_create

GITHUB_PROTECT_MASTER_RULESET := """
{
  "name": "Protect master from force pushes",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "include": ["refs/heads/master"],
      "exclude": []
    }
  },
  "rules": [
    {
      "type": "non_fast_forward"
    }
  ]
}
"""

_github_repo:
  gh repo view --json nameWithOwner -q .nameWithOwner

# TODO this only supports deleting the single ruleset specified above
github_ruleset_protect_master_delete:
  repo=$(just _github_repo) && \
    ruleset_name=$(echo '{{GITHUB_PROTECT_MASTER_RULESET}}' | jq -r .name) && \
    ruleset_id=$(gh api repos/$repo/rulesets --jq ".[] | select(.name == \"$ruleset_name\") | .id") && \
    (([ -n "${ruleset_id}" ] || (echo "No ruleset found" && exit 0)) || gh api --method DELETE repos/$repo/rulesets/$ruleset_id)

# adds github ruleset to prevent --force and other destructive actions on the github main branch
github_ruleset_protect_master_create: github_ruleset_protect_master_delete
  gh api --method POST repos/$(just _github_repo)/rulesets --input - <<< '{{GITHUB_PROTECT_MASTER_RULESET}}'

# Output logs of the last failed 'build' workflow for the current branch
[script]
github_last_build_failure:
    BRANCH=$(git branch --show-current)

    # 1. Fetch last 20 runs (to skip over 'Metadata Sync', 'Dependabot', etc.)
    JSON=$(gh run list -b "$BRANCH" -L 20 --json databaseId,conclusion,workflowName)

    # 2. Filter: Find the latest run where name contains "build" (case-insensitive)
    TARGET=$(echo "$JSON" | jq 'map(select(.workflowName | test("build"; "i"))) | .[0]')

    # 3. Handle case where no build run is found
    if [[ "$TARGET" == "null" ]]; then
        echo "No 'build' workflows found in the last 20 runs for $BRANCH."
        exit 0
    fi

    # 4. Extract Status and ID
    CONCLUSION=$(echo "$TARGET" | jq -r .conclusion)
    ID=$(echo "$TARGET" | jq -r .databaseId)

    # 5. Check Success vs Failure
    if [[ "$CONCLUSION" == "success" ]]; then
        echo "latest build succeeded"
    else
        # Force cat pager to output logs directly to terminal
        GH_PAGER=cat gh run view "$ID" --log-failed
    fi

# Set GitHub Actions permissions for the repository to allow workflows to write and approve PR reviews
# This enables release-please to run without a personal access token
github_repo_permissions_create:
  repo_path=$(gh repo view --json nameWithOwner --jq '.nameWithOwner') && \
    gh api --method PUT "/repos/${repo_path}/actions/permissions/workflow" \
      -f default_workflow_permissions=write \
      -F can_approve_pull_request_reviews=true && \
    gh api "/repos/${repo_path}/actions/permissions/workflow"

github_repo_set_metadata:
  gh repo edit \
    --description "$(yq  '.project.description' pyproject.toml)" \
    --homepage "$(yq '.project.urls.Repository' pyproject.toml)" \
    --add-topic "$(yq '.project.keywords | join(",")' pyproject.toml)"
