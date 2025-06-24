#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import importlib.util
from operator import itemgetter
from pathlib import Path
import argparse
import utf8totex

import ads


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


def main():
    parser = argparse.ArgumentParser(
        description="Update papers and resume stats from ADS."
    )
    parser.add_argument(
        "-o",
        "--output",
        default="data/pubs.json",
        help="Output JSON file for papers",
    )
    parser.add_argument(
        "--orcid", default="0000-0002-4296-2246", help="ORCID identifier"
    )
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    root = here.parent

    ads_key = json.load(open(root / "data" / "contact.json"))["ads_key"]
    ads.config.token = ads_key

    json_path = root / args.output

    spec = importlib.util.spec_from_file_location(
        "utf8totex", str(here / "utf8totex.py")
    )
    utf8totex = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(utf8totex)

    _papers = get_papers(args.orcid)
    papers = {
        "publications": [
            p
            for p in _papers
            if p["doctype"] not in ["dataset", "proposal", "abstract"]
            and p["arxiv"] is not None
        ]
    }
    papers["stats"] = {
        "total": len(papers["publications"]),
        "citations": sum([p["citations"] for p in papers["publications"]]),
    }

    with open(json_path, "w") as f:
        json.dump(papers, f, sort_keys=True, indent=2, separators=(",", ": "))


if __name__ == "__main__":
    main()
