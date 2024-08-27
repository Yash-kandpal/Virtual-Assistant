import os

import openai

openai.api_key = 'sample_sk-FvUfzuUMBd4uFWnpXECIT3BlbkFJpq7wtc0w4FelylKhiWLgyash'

response = openai.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Define friendship",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
