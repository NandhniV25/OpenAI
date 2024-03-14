from PyPDF2 import PdfReader, PdfWriter


def add_watermark(input_pdf_path, output_pdf_path, watermark_text):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    watermark_page = PdfReader(watermark_text)
    watermark_page = watermark_page.pages[0]

    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_pdf_path, 'wb') as output_pdf:
        writer.write(output_pdf)


input_pdf_path = "C:/Users/nandh/Downloads/case11.3.2024.pdf"
output_pdf_path = "./output.pdf"
watermark_text = "./watermark.pdf"
add_watermark(input_pdf_path, output_pdf_path, watermark_text)
