#!/usr/bin/env python3
"""Test skill discovery."""

import os
import sys
import yaml
from pathlib import Path

def find_skills():
    """Find all skills in .opencode/skills directory."""
    skills = []
    skill_dir = Path(".opencode/skills")
    if not skill_dir.exists():
        return skills
    
    for item in skill_dir.iterdir():
        if item.is_dir():
            skill_file = item / "SKILL.md"
            if skill_file.exists():
                # Parse frontmatter
                content = skill_file.read_text()
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        frontmatter = parts[1]
                        try:
                            data = yaml.safe_load(frontmatter)
                            if data and "name" in data:
                                skills.append({
                                    "name": data["name"],
                                    "description": data.get("description", ""),
                                    "path": str(item),
                                })
                        except yaml.YAMLError as e:
                            print(f"Error parsing YAML in {skill_file}: {e}")
    return skills

if __name__ == "__main__":
    skills = find_skills()
    print(f"Found {len(skills)} skills:")
    for skill in skills:
        print(f"  • {skill['name']}: {skill['description']}")
        # Check for script
        script_path = Path(skill["path"]) / "skill.py"
        if script_path.exists():
            print(f"    Script: {script_path}")
        else:
            print(f"    No script")