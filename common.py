import os


def get_list_of_files_in_directory(directory: str) -> list:
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith("txt"):
            files_names.append(filename)
    return files_names
