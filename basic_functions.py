import re

def extract_president_name(file_name: str) -> list:
    president_name = re.sub(r'\d', '', file_name)
    president_name = file_name[11:-4]
    return president_name

def extract_president_names(files_names: list) -> list:
    president_names = set()
    for file_name in files_names:
        file_name = re.sub(r'\d', '', file_name)
        file_name = file_name[11:-4]
        president_names.add(file_name)
    return list(president_names)


def associate_president_name_with_first_name(files_names: list) -> list:
    president_names = extract_president_name(files_names)
    president_names_with_first_name = []
    for president_name in president_names:
        match president_name:
            case "Chirac":
                president_names_with_first_name.append("Jacques Chirac")
            case "Giscard dEstaing":
                president_names_with_first_name.append("Valery Giscard d'Estaing")
            case "Hollande":
                president_names_with_first_name.append("François Hollande")
            case "Macron":
                president_names_with_first_name.append("Emmanuel Macron")
            case "Mitterrand":
                president_names_with_first_name.append("François Mitterrand")
            case "Sarkozy":
                president_names_with_first_name.append("Nicolas Sarkozy")
            case _:
                president_names_with_first_name.append(president_name)
    return president_names_with_first_name


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text) # enlève la ponctuation notamment les apostrophes et les tirets les remplace par un espace
    text = re.sub(r'\s+', ' ', text) # enlève les espaces multiples
    return text


def get_cleaned_speeches(files_names: list):
    for filename in files_names:
        with open("./speeches/" + filename, "r", encoding="utf-8") as file:
            cleaned_text = clean_text(file.read())
            with open("./cleaned/" + filename, 'w', encoding="utf-8") as cleaned_file:
                cleaned_file.write(cleaned_text)
