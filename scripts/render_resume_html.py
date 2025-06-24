import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import re
import argparse


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


def main():
    parser = argparse.ArgumentParser(description="Render resume HTML from JSON.")
    parser.add_argument(
        "-r", "--resume", default="data/resume.json", help="Resume JSON file"
    )
    parser.add_argument(
        "-p", "--pubs", default=None, help="Publications JSON file (optional)"
    )
    parser.add_argument(
        "-o", "--output", default="resume.html", help="Output HTML file"
    )
    args = parser.parse_args()

    here = Path(__file__).parent
    root = here.parent
    resume_path = root / args.resume
    template_name = "resume_template.html"
    output_path = root / args.output

    # Load resume data
    with open(resume_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Optionally load publications and add to data
    if args.pubs:
        pubs_path = root / args.pubs
        with open(pubs_path, "r", encoding="utf-8") as f:
            data["stats"] = json.load(f)["stats"]

    # Convert markdown links to HTML in all relevant fields
    data["stats"] = md_to_html(data.get("stats", ""))
    data["stack"] = md_to_html(data.get("technical_stack", ""))
    data["experience"] = convert_links_in_experience(data.get("experience", []))

    # Set up Jinja2 environment (load from project root)
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(str(template_name))

    # Render template
    html = template.render(**data)

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Resume rendered to {output_path}")


if __name__ == "__main__":
    main()
