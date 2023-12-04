import math
import os

from common import get_list_of_files_in_directory


def get_list_of_words(file: str) -> list:
    file = open("./cleaned/" + file, "r", encoding="utf-8")
    return list(set(file.read().split(" ")[:-1]))

def get_term_frequency(file: str) -> dict:
    list_of_words = get_list_of_words(file)
    term_frequency = {}
    fileLines = open("./cleaned/" + file, "r", encoding="utf-8").read().split(" ")
    for word in fileLines:
        if word not in term_frequency.keys():
            term_frequency[word] = 1
        else:
            term_frequency[word] += 1
    return term_frequency




def get_inverse_document_frequency(directory: str) -> dict:
    files_names = get_list_of_files_in_directory("./cleaned")
    corpus_size = len(files_names)
    document_frequency = {}
    allWords = []
    for i in (os.listdir(("./cleaned/"))):
        allWords += get_list_of_words(i)
    allWords = list(set(allWords))
    for word in allWords:
        for i in (os.listdir(("./cleaned/"))):
            texte = open("./cleaned/" + i, "r", encoding="utf-8").read()
            if word in texte:
                if word not in document_frequency.keys():
                    document_frequency[word] = 1
                else:
                    document_frequency[word] += 1
    inverse_document_frequency = {}
    for word in document_frequency.keys():
        inverse_document_frequency[word] = math.log10(8 / document_frequency[word])
    return inverse_document_frequency


def get_tf_id_matrix(directory: str) -> list:
    files_names = get_list_of_files_in_directory("./cleaned")
    tf_id_matrix = []
    inverse_document_frequency = get_inverse_document_frequency(directory)
    list_of_words = inverse_document_frequency.keys()
    word_list = []
    for word in list_of_words :
        word_list.append(word)
        word_idf_score = inverse_document_frequency[word]
        word_tf_idf_scores = []
        for file_name in files_names:
            tf_scores = get_term_frequency(file_name)
            if word in get_list_of_words(file_name):
                word_tf_score = tf_scores[word]
            else :
                word_tf_score = 0
            word_tf_idf_score = word_tf_score*word_idf_score
            word_tf_idf_scores.append(word_tf_idf_score)
        tf_id_matrix.append(word_tf_idf_scores)
    return tf_id_matrix, word_list


def mots_pas_importants(matrice, liste_de_mots):
    nombre_textes = len(matrice[0])
    score_nul = [0.0]*nombre_textes
    mots_pas_importants = []
    for i in range(len(matrice)):
        if matrice[i] == score_nul :
            mots_pas_importants.append(liste_de_mots[i])
    return mots_pas_importants

def mots_importants(matrice, liste_de_mots):
    mots_importants = [liste_de_mots[0]]
    score = 0
    for i in range(len(matrice[0])):
        score += matrice[0][i]
    max = score
    for i in range(1,len(matrice)):
        score = 0
        for j in range(len(matrice[i])):
            score += matrice[i][j]
        if score >= max :
            if score > max :
                max = score
                mots_importants.clear()
            mots_importants.append(liste_de_mots[i])
    return mots_importants



if __name__ == "__main__":
    print(get_term_frequency("Nomination_Chirac1.txt"))
    print(get_inverse_document_frequency("./cleaned"))
    matrice, word_list = get_tf_id_matrix("./cleaned")
    print(mots_importants(matrice, word_list))

