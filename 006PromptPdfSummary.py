import openai
import os
import PyPDF2

openai.api_key = os.getenv('OPENAI_API_kEY')


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]


def readPdfFile(filePath):
    with open(filePath, 'rb') as file:
        page_reader = PyPDF2.PdfReader(file)
        num_pages = len(page_reader.pages)
        ans = ""
        for page_num in range(num_pages):
            page = page_reader.pages[page_num]
            text = page.extract_text()
            ans += text
    return ans


# print(readPdfFile("C:\\Nandhni\\GitRepo\\OpenAI\\Education.pdf"))

text = readPdfFile("C:\\Nandhni\GitRepo\OpenAI\Education.pdf")
# print(text)
prompt = f"""Your task is to generate summary for the given text\
    delimited by triple backticks. \
        ```{text}``` 
        """

response = get_completion(prompt)
print(response)
