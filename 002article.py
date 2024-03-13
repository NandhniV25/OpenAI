import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


topic = f"""Write an article on the purpose of Technology"""

prompt = f"""Your task is to generate an article
on the topic which is delimited by triple backticks.
```{topic}```
"""

response = get_completion(prompt)
print(response)

prompt = f"""Your task is to generate the article\
for the topic delimited by triple backticks
in 50 words ```{topic}```, 
"""
response = get_completion(prompt)
print(response)
