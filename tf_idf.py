import math
from common import get_list_of_files_in_directory


def get_list_of_words(file: str) -> list:
    file = open("./cleaned/" + file, "r", encoding="utf-8")
    return file.read().split(" ")[:-1]


def get_term_frequency(file: str) -> dict:
    list_of_words = get_list_of_words(file)
    term_frequency = {}
    for word in list_of_words:
        if word not in term_frequency.keys():
            term_frequency[word] = 1
        else:
            term_frequency[word] += 1
    for word in term_frequency.keys():
        term_frequency[word] = term_frequency[word] / len(list_of_words)
    return term_frequency


def get_inverse_document_frequency(directory: str) -> dict:
    files_names = get_list_of_files_in_directory("./cleaned")
    corpus_size = len(files_names)
    document_frequency = {}
    for file_name in files_names:
        list_of_words = get_list_of_words(file_name)
        for word in list_of_words:
            if word not in document_frequency.keys():
                document_frequency[word] = 1
            else:
                document_frequency[word] += 1
    inverse_document_frequency = {}
    for word in document_frequency.keys():
        inverse_document_frequency[word] = math.log(corpus_size / document_frequency[word] + 1)
    return inverse_document_frequency


def get_tf_id_matrix(directory: str) -> list:
    files_names = get_list_of_files_in_directory("./cleaned")
    tf_id_matrix = []
    inverse_document_frequency = get_inverse_document_frequency(directory)
    for file_name in files_names:
        term_frequency = get_term_frequency(file_name)
        tf_id_vector = []
        for word in inverse_document_frequency.keys():
            if word in term_frequency.keys():
                tf_id_vector.append(term_frequency[word] * inverse_document_frequency[word])
            else:
                tf_id_vector.append(0)
        tf_id_matrix.append(tf_id_vector)
    return tf_id_matrix
