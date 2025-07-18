# render.py
from weasyprint import HTML

HTML("index.html").write_pdf("output_resume.pdf")
print("Generated output_resume.pdf")
