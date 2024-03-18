import PyPDF2
with open('C:/Users/nandh/Downloads/case11.3.2024.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    # print(type(file))
    # print(type(reader))
    num_pages = len(reader.pages)
    # print(type(num_pages))
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        # print(type(page))
        text = page.extract_text()
        # print(type(text))
        # print(f"Page {page_num + 1}:\n{text}\n")
        try:
            print(f"Page {page_num + 1}:\n{text}\n")
        except UnicodeEncodeError:
            # If encoding fails, print a message indicating the issue
            print(
                f"Page {page_num + 1} contains characters that cannot be encoded")
