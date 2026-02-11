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
