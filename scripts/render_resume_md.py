import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser(description="Render resume Markdown from JSON.")
    parser.add_argument(
        "-r", "--resume", default="data/resume_en.json", help="Resume JSON file"
    )
    parser.add_argument(
        "-p", "--pubs", default=None, help="Publications JSON file (optional)"
    )
    parser.add_argument(
        "-o", "--output", default="readme.md", help="Output Markdown file"
    )
    args = parser.parse_args()

    here = Path(__file__).parent
    root = here.parent
    resume_path = root / args.resume
    template_name = "resume_template.md"
    output_path = root / args.output

    # Load resume data
    with open(resume_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Optionally load publications and add to data
    if args.pubs:
        pubs_path = root / args.pubs
        with open(pubs_path, "r", encoding="utf-8") as f:
            data["stats"] = json.load(f)["stats"]

    # Set up Jinja2 environment (load from project root)
    env = Environment(
        loader=FileSystemLoader(str(root)), trim_blocks=True, lstrip_blocks=True
    )
    template = env.get_template(str(template_name))

    # Render template
    md = template.render(**data)

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Markdown resume written to {output_path}")


if __name__ == "__main__":
    main()
