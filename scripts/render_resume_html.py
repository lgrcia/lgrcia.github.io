import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import re


# Helper to convert markdown links to HTML links
def md_to_html(text):
    if not isinstance(text, str):
        return text

    # links
    converted = re.sub(r"\[([^\]]+)\]\(([^\)]+)\)", r'<a href="\2">\1</a>', text)
    # bold
    converted = re.sub(r"\*\*([^\*]+)\*\*", r"<strong>\1</strong>", converted)
    # italics
    converted = re.sub(r"\*([^\*]+)\*", r"<i>\1</i>", converted)
    return converted


def convert_links_in_list(lst):
    return [md_to_html(item) for item in lst]


def convert_links_in_experience(experience):
    for job in experience:
        job["description"] = convert_links_in_list(job["description"])
    return experience


# Paths
here = Path(__file__).parent
root = here.parent
json_path = root / "data" / "resume.json"
template_name = "resume_template.html"
# output_dir = root / "build"
# output_dir.mkdir(exist_ok=True)
output_path = root / "resume.html"

# Load data
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert markdown links to HTML in all relevant fields
data["stats"] = md_to_html(data.get("stats", ""))
data["stack"] = md_to_html(data.get("technical_stack", ""))
data["experience"] = convert_links_in_experience(data.get("experience", []))

# Set up Jinja2 environment (load from project root)
env = Environment(loader=FileSystemLoader("."))
template = env.get_template(template_name)

# Render template
html = template.render(**data)

# Write output
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Resume rendered to {output_path}")
