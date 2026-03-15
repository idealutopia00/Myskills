#!/usr/bin/env python3
"""CLI for MySkills platform."""

import os
import sys
import yaml
import click
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
                        except yaml.YAMLError:
                            pass
    return skills

@click.group()
def cli():
    """MySkills - Multi-skill platform for OpenCode agents."""
    pass

@cli.command("list")
def list_skills():
    """List all available skills."""
    skills = find_skills()
    if not skills:
        click.echo("No skills found.")
        return
    
    click.echo(f"Found {len(skills)} skills:")
    for skill in skills:
        click.echo(f"  • {skill['name']}: {skill['description']}")

@cli.command("run")
@click.argument("skill_name")
@click.argument("input", required=False)
def run_skill(skill_name, input):
    """Run a specific skill with optional input."""
    skills = find_skills()
    skill = next((s for s in skills if s["name"] == skill_name), None)
    if not skill:
        click.echo(f"Skill '{skill_name}' not found.")
        return
    
    click.echo(f"Running skill: {skill['name']}")
    click.echo(f"Description: {skill['description']}")
    
    # Check for skill script
    skill_path = Path(skill["path"])
    script_path = skill_path / "skill.py"
    if script_path.exists():
        click.echo(f"Executing script: {script_path}")
        # In a real implementation, you would import and run the script
        click.echo("(Script execution would happen here)")
    else:
        click.echo("No executable script found. Skill definition only.")

if __name__ == "__main__":
    cli()