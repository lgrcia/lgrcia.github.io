import re
import json
from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser(description="Convert resume.md to resume.json")
    parser.add_argument(
        "-i", "--input", default="resume.md", help="Input Markdown file"
    )
    parser.add_argument(
        "-o", "--output", default="data/resume.json", help="Output JSON file"
    )
    args = parser.parse_args()

    here = Path(__file__).parent
    md_path = (
        str(here.parent / args.input)
        if not Path(args.input).is_absolute()
        else args.input
    )
    json_path = (
        str(here.parent / args.output)
        if not Path(args.output).is_absolute()
        else args.output
    )

    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    resume = {}

    # Parse name
    for i, line in enumerate(lines):
        if line.startswith("# "):
            resume["name"] = line.strip("# \n")
            start = i + 1
            break

    # Parse summary (first non-empty line after name)
    summary = ""
    for line in lines[start:]:
        if line.strip():
            summary = line.strip()
            break
    resume["summary"] = summary

    # Parse stats and stack
    stats = []
    stack = ""
    for line in lines:
        if line.startswith("- As of") or line.startswith("- As Of"):
            stats.append(line.strip("- \n"))
        if line.startswith("- Technical stack"):
            stack = line.strip("- \n")
    resume["stats"] = stats
    resume["technical_stack"] = stack

    # Parse Experience
    exp_section = []
    exp_start = False
    for line in lines:
        if line.strip().startswith("## Experience"):
            exp_start = True
            continue
        if exp_start and line.strip().startswith("## "):
            break
        if exp_start:
            exp_section.append(line)

    # Parse each experience
    experiences = []
    exp = {}
    desc = []
    for line in exp_section:
        m = re.match(r"\*\*(.+)\*\*", line)
        if m:
            if exp:
                exp["description"] = desc
                experiences.append(exp)
                exp = {}
                desc = []
            exp["title"] = m.group(1)
            continue
        m = re.match(r"\*(.+)\*", line)
        if m and "location" not in exp:
            exp["location"] = m.group(1)
            continue
        if line.strip().startswith("-"):
            desc.append(line.strip("- \n"))
    if exp:
        exp["description"] = desc
        experiences.append(exp)
    resume["experience"] = experiences

    # Parse Education
    edu_section = []
    edu_start = False
    for line in lines:
        if line.strip().startswith("## Education"):
            edu_start = True
            continue
        if edu_start and line.strip().startswith("## "):
            break
        if edu_start:
            edu_section.append(line)

    educations = []
    edu = {}
    for line in edu_section:
        m = re.match(r"- \*\*(.+)\*\*", line)
        if m:
            if edu:
                educations.append(edu)
                edu = {}
            edu["degree"] = m.group(1)
            continue
        m2 = re.match(r"\s+(.+)", line)
        if m2 and "degree" in edu:
            edu["location"] = m2.group(1).strip()
    if edu:
        educations.append(edu)
    resume["education"] = educations

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(resume, f, indent=2, ensure_ascii=False)

    print(f"Resume parsed and saved to {json_path}")


if __name__ == "__main__":
    main()
