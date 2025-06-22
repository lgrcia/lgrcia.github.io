import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

# Paths
here = Path(__file__).parent
root = here.parent
json_path = root / "data" / "resume.json"
template_name = "resume_template.md"
output_path = root / "readme.md"

# Load data
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Set up Jinja2 environment (load from project root)
env = Environment(
    loader=FileSystemLoader(str(root)), trim_blocks=True, lstrip_blocks=True
)
template = env.get_template(template_name)

# Render template
md = template.render(**data)

# Write output
with open(output_path, "w", encoding="utf-8") as f:
    f.write(md)

print(f"Markdown resume written to {output_path}")
