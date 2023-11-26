import os
import re


def get_list_of_files_in_directory(directory: str) -> list:
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith("txt"):
            files_names.append(filename)
    return files_names


directory = "./speeches"
files_names = get_list_of_files_in_directory(directory)


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text


def get_cleaned_speeches(files_names: list):
    for filename in files_names:
        with open("./speeches/" + filename, "r", encoding="utf-8") as file:
            cleaned_text = clean_text(file.read())
            with open("./cleaned/" + filename, 'w', encoding="utf-8") as file:
                file.write(cleaned_text)
