all:
	python scripts/update_papers.py
	python scripts/render_resume_html.py
	python scripts/render_resume_md.py
	typst compile resume.typ build/resume.pdf