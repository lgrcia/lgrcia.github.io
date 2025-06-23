#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import importlib.util
from operator import itemgetter
from pathlib import Path

import ads

ads_key = json.load(open(Path(__file__).parent.parent / "data" / "contact.json"))[
    "ads_key"
]
ads.config.token = ads_key

here = Path(__file__).resolve().parent
json_path = here.parent / "data" / "pubs.json"

spec = importlib.util.spec_from_file_location("utf8totex", str(here / "utf8totex.py"))
utf8totex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(utf8totex)


def get_papers(orcid):
    papers = list(
        ads.SearchQuery(
            orcid=orcid,
            fl=[
                "id",
                "title",
                "author",
                "doi",
                "year",
                "pubdate",
                "pub",
                "volume",
                "page",
                "identifier",
                "doctype",
                "citation_count",
                "bibcode",
            ],
            max_pages=100,
        )
    )
    dicts = []
    for paper in papers:
        if paper.identifier is None:
            continue
        aid = [
            ":".join(t.split(":")[1:])
            for t in paper.identifier
            if t.startswith("arXiv:")
        ]
        for t in paper.identifier:
            if len(t.split(".")) != 2:
                continue
            try:
                list(map(int, t.split(".")))
            except ValueError:
                pass
            else:
                aid.append(t)
        try:
            page = int(paper.page[0])
        except (ValueError, TypeError):
            page = None
            if paper.page is not None and paper.page[0].startswith("arXiv:"):
                aid.append(":".join(paper.page[0].split(":")[1:]))
        dicts.append(
            dict(
                doctype=paper.doctype,
                authors=list(map(utf8totex.utf8totex, paper.author)),
                year=paper.year,
                pubdate=paper.pubdate,
                doi=paper.doi[0] if paper.doi is not None else None,
                title=utf8totex.utf8totex(paper.title[0].replace(" &amp; ", " & ")),
                pub=paper.pub,
                volume=paper.volume,
                page=page,
                arxiv=aid[0] if len(aid) else None,
                citations=(
                    paper.citation_count if paper.citation_count is not None else 0
                ),
                url="https://ui.adsabs.harvard.edu/abs/" + paper.bibcode,
            )
        )
    return sorted(dicts, key=itemgetter("pubdate"), reverse=True)


if __name__ == "__main__":
    papers = get_papers("0000-0002-4296-2246")
    papers = [
        p for p in papers if p["doctype"] not in ["dataset", "proposal", "abstract"]
    ]
    with open(json_path, "w") as f:
        json.dump(papers, f, sort_keys=True, indent=2, separators=(",", ": "))

    resume_json = here.parent / "resume.json"
    with open(resume_json, "r") as f:
        resume = json.load(f)

    total_papers = len(papers)
    total_citations = sum([p["citations"] for p in papers])

    from datetime import datetime

    current_date = datetime.now().strftime("%Y-%m-%d")

    resume["stats"] = (
        f"{total_papers} refereed publications, {total_citations} total citations."
    )

    print(f"total papers: {total_papers}")
    print(f"total citations: {total_citations}")

    with open(resume_json.parent / "data" / "resume.json", "w") as f:
        json.dump(resume, f, indent=2, ensure_ascii=False)
