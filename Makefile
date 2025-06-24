all:
	mkdir -p build
	python scripts/update_papers.py -o data/pubs.json
# English
	python scripts/render_resume_html.py -r resume_en.json -p data/pubs.json -o build/resume_en.html
	typst compile --input lang=en resume.typ build/resume_en.pdf
# French
	python scripts/render_resume_html.py -r resume_fr.json -p data/pubs.json -o build/resume_fr.html
	typst compile --input lang=fr resume.typ build/resume_fr.pdf
	
	python scripts/render_resume_md.py -r resume_en.json -p data/pubs.json -o readme.md
	