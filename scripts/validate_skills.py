#!/usr/bin/env python3
"""
Ministry AI Skills Validator
Validates that all skills follow the standardized 6-file anatomy and match catalog.json.
Lightweight, dependency-free script using Python standard library.
"""

import json
import os
import sys
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "prompt.md",
    "inputs.schema.json",
    "workflow.md",
    "guardrails.md",
    "examples.md",
]

VALID_SENSITIVITIES = {"low", "medium", "high"}

def validate_repository(root_dir: Path) -> bool:
    skills_dir = root_dir / "skills"
    catalog_path = skills_dir / "catalog.json"
    has_errors = False

    print("==========================================")
    print("  Ministry AI Skills - Repository Linter")
    print("==========================================\n")

    if not catalog_path.is_file():
        print(f"[FAIL] Missing catalog file: {catalog_path}")
        return False

    # 1. Validate catalog.json structure
    try:
        with open(catalog_path, "r", encoding="utf-8") as f:
            catalog_data = json.load(f)
        print(f"[OK] catalog.json is valid JSON.")
    except Exception as e:
        print(f"[FAIL] catalog.json parsing error: {e}")
        return False

    catalog_skills = catalog_data.get("skills", [])
    catalog_skill_ids = {s.get("id") for s in catalog_skills if "id" in s}
    declared_total = catalog_data.get("total_skills", 0)

    if len(catalog_skills) != declared_total:
        print(f"[WARN] catalog.json 'total_skills' ({declared_total}) does not match skill count ({len(catalog_skills)}).")

    # 2. Discover skill directories
    discovered_skill_dirs = [
        d for d in skills_dir.iterdir()
        if d.is_dir() and not d.name.startswith((".", "_"))
    ]

    print(f"\n[INFO] Found {len(discovered_skill_dirs)} skill directories.")

    # 3. Check each skill folder
    for skill_dir in sorted(discovered_skill_dirs, key=lambda p: p.name):
        skill_id = skill_dir.name
        print(f"\n--> Checking skill: {skill_id}")

        # Check required files
        for req_file in REQUIRED_FILES:
            file_path = skill_dir / req_file
            if not file_path.is_file():
                print(f"    [FAIL] Missing required file: {req_file}")
                has_errors = True
            elif file_path.stat().st_size == 0:
                print(f"    [FAIL] Required file is empty: {req_file}")
                has_errors = True
            else:
                print(f"    [OK] Found {req_file}")

        # Validate inputs.schema.json
        schema_path = skill_dir / "inputs.schema.json"
        schema_json = None
        if schema_path.is_file():
            try:
                with open(schema_path, "r", encoding="utf-8") as sf:
                    schema_json = json.load(sf)
                if not isinstance(schema_json, dict) or schema_json.get("type") != "object":
                    print("    [FAIL] inputs.schema.json root must be a JSON object with 'type': 'object'.")
                    has_errors = True
                else:
                    print("    [OK] inputs.schema.json format valid.")
            except Exception as e:
                print(f"    [FAIL] inputs.schema.json invalid JSON: {e}")
                has_errors = True

        # Check presence in catalog.json
        matching_catalog = next((s for s in catalog_skills if s.get("id") == skill_id), None)
        if not matching_catalog:
            print(f"    [FAIL] Skill '{skill_id}' is not indexed in skills/catalog.json.")
            has_errors = True
        else:
            print(f"    [OK] Skill '{skill_id}' indexed in catalog.json.")
            
            # Check sensitivity level
            sensitivity = matching_catalog.get("sensitivity_level")
            if sensitivity not in VALID_SENSITIVITIES:
                print(f"    [FAIL] Invalid sensitivity_level '{sensitivity}' in catalog. Expected one of {VALID_SENSITIVITIES}.")
                has_errors = True
            
            # Check required_inputs against schema
            if schema_json and "required" in schema_json:
                schema_required = set(schema_json.get("required", []))
                catalog_required = set(matching_catalog.get("required_inputs", []))
                if schema_required != catalog_required:
                    print(f"    [FAIL] required_inputs mismatch in catalog.json for '{skill_id}'. Schema: {schema_required}, Catalog: {catalog_required}")
                    has_errors = True
                else:
                    print(f"    [OK] required_inputs match schema specification.")

    # 4. Check for orphaned catalog entries
    for s in catalog_skills:
        s_id = s.get("id")
        if s_id and not (skills_dir / s_id).is_dir():
            print(f"[FAIL] Catalog lists skill '{s_id}', but folder does not exist at skills/{s_id}")
            has_errors = True

    # 5. Check template anatomy
    template_dir = root_dir / "templates" / "skill-template"
    if template_dir.is_dir():
        print(f"\n--> Checking template: templates/skill-template")
        for req_file in REQUIRED_FILES:
            tf = template_dir / req_file
            if not tf.is_file():
                print(f"    [FAIL] Template missing file: {req_file}")
                has_errors = True
            else:
                print(f"    [OK] Template has {req_file}")

    print("\n==========================================")
    if has_errors:
        print("  Validation FAILED: Please fix errors above.")
        print("==========================================")
        return False
    else:
        print("  Validation PASSED: All skills & catalog clean!")
        print("==========================================")
        return True

if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parent.parent
    success = validate_repository(repo_root)
    sys.exit(0 if success else 1)
