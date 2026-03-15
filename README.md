# MySkills: Multi-Skill Platform for OpenCode

A platform for defining and using reusable skills with OpenCode agents. Each skill combines OpenCode skill definitions with executable scripts for common daily tasks.

## Features

- **OpenCode-compatible skill definitions**: Follows OpenCode's SKILL.md specification
- **Script integration**: Each skill can have associated Python scripts for automation
- **CLI interface**: List and run skills from command line
- **Extensible architecture**: Easy to add new skills

## Directory Structure

```
.opencode/skills/          # OpenCode skill definitions
  <skill-name>/
    SKILL.md              # Skill definition (frontmatter + instructions)
    skill.py              # Optional executable script (example)
src/myskills/             # Platform CLI and utilities
  cli.py                  # Command-line interface
requirements.txt          # Python dependencies
.opencode.json            # OpenCode configuration
```

## Available Skills

1. **literature-review**: Read academic literature and generate comprehensive reading notes
2. **daily-standup**: Generate daily standup notes for agile teams
3. **code-review**: Conduct thorough code reviews with focus on quality, security, performance
4. **meeting-notes**: Generate comprehensive meeting notes with action items and decisions

## Usage

### With OpenCode Agents

OpenCode agents can discover and load skills using the native `skill` tool:

```bash
# In OpenCode session, agent can:
skill({ name: "literature-review" })
```

The agent will see the skill description and follow the instructions in SKILL.md.

### With CLI Tool

Install dependencies:

```bash
pip install -r requirements.txt
```

List available skills:

```bash
python -m myskills.cli list
```

Run a skill:

```bash
python -m myskills.cli run literature-review
```

### Adding New Skills

1. Create a directory in `.opencode/skills/<skill-name>/`
2. Add `SKILL.md` with frontmatter and instructions
3. Optionally add executable scripts (e.g., `skill.py`)

Example SKILL.md:

```markdown
---
name: my-skill
description: Brief description of what the skill does
license: MIT
compatibility: opencode
---

## What I do
- Task 1
- Task 2

## When to use me
Use this skill when...
```

## Development

The platform includes a Python CLI for managing skills. The `src/myskills/cli.py` provides basic listing and execution functionality.

To extend:

1. Add skill scripts with proper argument parsing
2. Enhance CLI with additional features
3. Create skill templates for common patterns

## License

MIT