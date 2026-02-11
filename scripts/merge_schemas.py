#!/usr/bin/env python
import json
import urllib.request
from pathlib import Path

import yaml
from jsonpath_ng import parse

# Manual JSON schema adjustments
MANUAL_ADJUSTMENTS = [
    {"path": "$.components.schemas.AttributionSource.properties.url", "updates": {"nullable": True}},
    {"path": "$.components.schemas.AttributionSource.required", "updates": {"remove_item": "url"}},
]

# Create directory and download files
Path("ghl_schema").mkdir(exist_ok=True)

print("Downloading custom-fields.json...")
urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/GoHighLevel/highlevel-api-docs/main/apps/custom-fields.json",
    "ghl_schema/custom-fields.json",
)

print("Downloading contacts.json...")
urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/GoHighLevel/highlevel-api-docs/main/apps/contacts.json",
    "ghl_schema/contacts.json",
)

# Merge specs
print("Merging OpenAPI specs...")
custom_fields = json.loads(Path("ghl_schema/custom-fields.json").read_text())
contacts = json.loads(Path("ghl_schema/contacts.json").read_text())


def snake_to_camel(snake_str):
    """Convert snake_case to camelCase"""
    components = snake_str.split("_")
    return components[0] + "".join(word.capitalize() for word in components[1:])


def apply_manual_adjustments(data):
    """Apply manual JSON schema adjustments using JSONPath"""
    for adjustment in MANUAL_ADJUSTMENTS:
        jsonpath_expr = parse(adjustment["path"])
        matches = jsonpath_expr.find(data)

        if matches:
            for match in matches:
                target = match.value
                updates = adjustment["updates"]

                # Handle special case: removing item from list
                if "remove_item" in updates:
                    if isinstance(target, list):
                        item_to_remove = updates["remove_item"]
                        if item_to_remove in target:
                            target.remove(item_to_remove)
                            print(f"  Removed '{item_to_remove}' from {adjustment['path']}")
                        else:
                            print(f"  Warning: '{item_to_remove}' not found in {adjustment['path']}")
                    else:
                        print(f"  Warning: {adjustment['path']} is not a list, cannot remove item")

                # Handle regular dict updates
                elif isinstance(target, dict):
                    target.update(updates)
                    print(f"  Applied adjustment to {adjustment['path']}: {updates}")
                else:
                    print(f"  Warning: {adjustment['path']} is not a dict, skipping")
        else:
            print(f"  Warning: {adjustment['path']} not found in schema")

    return data


# some keys are reported as snake_case from the API, but are actually camelCase
def fix_property_keys(obj):
    """Recursively fix property keys from snake_case to camelCase in OpenAPI schemas"""
    if isinstance(obj, dict):
        # Check if this looks like a schema properties object
        if "properties" in obj and isinstance(obj["properties"], dict):
            new_properties = {}
            for key, value in obj["properties"].items():
                # Convert snake_case keys to camelCase
                if "_" in key:
                    camel_key = snake_to_camel(key)
                    print(f"  Converting property: {key} -> {camel_key}")
                    new_properties[camel_key] = fix_property_keys(value)
                else:
                    new_properties[key] = fix_property_keys(value)
            obj["properties"] = new_properties

        # Recursively process other dict values
        return {k: fix_property_keys(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [fix_property_keys(item) for item in obj]
    else:
        return obj


# Fix property keys in contacts schema and apply manual adjustments
print("Converting snake_case properties to camelCase in contacts schema...")
contacts = fix_property_keys(contacts)

print("Applying manual schema adjustments to contacts schema...")
contacts = apply_manual_adjustments(contacts)

# Save the updated contacts.json with camelCase properties and manual adjustments
Path("ghl_schema/contacts.json").write_text(json.dumps(contacts, indent=2))
print("Updated contacts.json with camelCase properties and manual adjustments")

# Start with custom-fields as base
merged = custom_fields.copy()

# Merge paths
merged["paths"].update(contacts.get("paths", {}))

# Merge components if they exist
if "components" in contacts:
    if "components" not in merged:
        merged["components"] = {}
    for key in contacts["components"]:
        if key not in merged["components"]:
            merged["components"][key] = {}
        merged["components"][key].update(contacts["components"][key])

# Update info to reflect merged nature
merged["info"]["title"] = "ghl"
merged["info"]["description"] = "GoHighLevel API - Custom Fields and Contacts endpoints"

# Write as YAML
Path("ghl_schema/combined.yaml").write_text(yaml.dump(merged, default_flow_style=False))
print("Successfully merged OpenAPI specs to ghl_schema/combined.yaml")
