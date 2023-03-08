import pdftotext
import openai
import csv

def split_string(text):
    max_length = 2500
    if len(text) <= max_length:
        return [text]

    split_index = text.rfind(".", 0, max_length)
    if split_index == -1:
        split_index = max_length

    left_text = text[:split_index + 1].strip()
    right_text = text[split_index + 1:].strip()

    return [left_text] + split_string(right_text)

with open('FILE NAME OF PDF GOES HERE', 'rb') as f:
    pdf = pdftotext.PDF(f)

    text = "\n\n".join(pdf)

parts = split_string(text)

overall_response = [""]


for part in parts:
    openai.api_key = "GET YOUR PRIVATE API KEY FROM OPENAPI"

    model_engine = "text-davinci-003"
    prompt = "Using the following provided text, please produce a html table with one column being the question and the other being the answer: " + part

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    overall_response.append(response)

delimiter = " "
final_response = delimiter.join(overall_response)
print(final_response)

with open("sample.html", mode='w', newline='') as file:
    file.write(final_response)
