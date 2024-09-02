import json
import re
import pdfplumber  # o PyPDF2, dependiendo de su preferencia
import csv
from datetime import datetime, date
import PyPDF2
from utils.process import process_document
from utils.save_csv import save_to_csv


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_content = page.extract_text()
            text = text + "\n" + page_content

    return text


# Uso
pdf_path = "docs/complete_code.pdf"
print(pdf_path)
text = extract_text_from_pdf(pdf_path)
structured_content = process_document(text)
# print(structured_content)
# Imprimir la estructura


def save_to_txt(txt):
    f = open(f"output/docs/doc{datetime.now().timetz()}.txt", "w")
    f.writelines(txt)
    f.close()


def save_data(data):
    with open("output/docs/sample.json", "w") as outfile:
        json.dump(data, outfile)


# Uso
csv_filename = f"output/code_estructurado-{datetime.now().timetz()}.csv"
save_to_csv(structured_content, csv_filename)
save_to_txt(text)
# save_data(structured_content)
