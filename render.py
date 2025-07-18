from weasyprint import HTML
HTML("index.html").write_pdf("output_resume.pdf")
