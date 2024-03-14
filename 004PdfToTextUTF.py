import PyPDF2


def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]

            text = page.extract_text()

            output_file_path = f"./extracted_page_{page_num + 1}.txt"
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(text)

            print(
                f"Page {page_num + 1}: Extracted text written to {output_file_path}")


pdf_file_path = 'C:/Users/nandh/Downloads/case11.3.2024.pdf'

read_pdf(pdf_file_path)
