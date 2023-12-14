import math
import os

from common import get_list_of_files_in_directory
from basic_functions import extract_president_name


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
    files_names = get_list_of_files_in_directory(directory)
    corpus_size = len(files_names)
    document_frequency = {}
    allWords = []
    for i in (os.listdir((directory))):
        allWords += get_list_of_words(i)
    allWords = list(set(allWords))
    for word in allWords:
        for i in (os.listdir((directory))):
            texte = open(directory + i, "r", encoding="utf-8").read()
            if word in texte:
                if word not in document_frequency.keys():
                    document_frequency[word] = 1
                else:
                    document_frequency[word] += 1
    inverse_document_frequency = {}
    for word in document_frequency.keys():
        inverse_document_frequency[word] = math.log10(corpus_size / document_frequency[word])
    return inverse_document_frequency


def get_tf_id_matrix(directory : str) -> list :
    files_names = get_list_of_files_in_directory(directory)
    tf_id_matrix = []
    inverse_document_frequency = get_inverse_document_frequency(directory)
    term_frequency_scores = []
    for i in range(len(files_names)):
        tf_score = get_term_frequency(files_names[i])
        term_frequency_scores.append(tf_score)
    list_of_words = inverse_document_frequency.keys()
    word_list = []
    for word in list_of_words:
        word_list.append(word)
        word_idf_score = inverse_document_frequency[word]
        word_tf_idf_scores = []
        for i in range(len(files_names)):
            tf_scores = term_frequency_scores[i]
            if word in get_list_of_words(files_names[i]):
                word_tf_score = tf_scores[word]
            else:
                word_tf_score = 0
            word_tf_idf_score = word_tf_score * word_idf_score
            word_tf_idf_scores.append(word_tf_idf_score)
        tf_id_matrix.append(word_tf_idf_scores)
    return tf_id_matrix, word_list



def mots_pas_importants(matrice: list, liste_de_mots: list) -> list:
    nombre_textes = len(matrice[0])
    score_nul = [0.0] * nombre_textes
    mots_pas_importants = []
    for i in range(len(matrice)):
        if matrice[i] == score_nul:
            mots_pas_importants.append(liste_de_mots[i])
    return mots_pas_importants


def mots_importants(matrice: list, liste_de_mots: list) -> list:
    mots_importants = [liste_de_mots[0]]
    score = 0
    for i in range(len(matrice[0])):
        score += matrice[0][i]
    max = score
    for i in range(1, len(matrice)):
        score = 0
        for j in range(len(matrice[i])):
            score += matrice[i][j]
        if score >= max:
            if score > max:
                max = score
                mots_importants.clear()
            mots_importants.append(liste_de_mots[i])
    return mots_importants


def mots_repetes_par(directory: str, president: str, mots_non_importants: list) -> list:
    score_des_mots = []
    liste_of_files = get_list_of_files_in_directory(directory)
    for i in range(len(liste_of_files)):
        if extract_president_name(liste_of_files[i]) == president:
            score_des_mots.append(get_term_frequency(liste_of_files[i]))
    score_global = {}
    if len(score_des_mots) == 1:
        score_global = score_des_mots[0]
    else:
        for key in score_des_mots[0].keys():
            score_global[key] = score_des_mots[0][key]
            if key in score_des_mots[1].keys():
                score_global[key] += score_des_mots[1][key]
        for key in score_des_mots[1].keys():
            if key not in score_des_mots[0].keys():
                score_global[key] = score_des_mots[1][key]
    max = 0
    liste_des_mots = []
    for key in score_global.keys():
        if key not in mots_non_importants:
            if score_global[key] >= max:
                if score_global[key] > max:
                    max = score_global[key]
                    liste_des_mots.clear()
                liste_des_mots.append(key)
    return liste_des_mots


def president_ayant_parle_de(directory: str, mot: str) -> list:
    liste_of_files = get_list_of_files_in_directory(directory)
    liste_des_presidents = []
    for file in liste_of_files:
        liste_des_mots = get_list_of_words(file)
        if mot in liste_des_mots:
            nom_president = extract_president_name(file)
            if nom_president not in liste_des_presidents:
                liste_des_presidents.append(nom_president)
    return liste_des_presidents


def mots_repetes_par_tous_les_presidents(directory: str, mots_non_importants: list) -> list:
    liste_of_files = get_list_of_files_in_directory(directory)
    liste_des_mots = get_list_of_words(liste_of_files[0])
    for i in range(1, len(liste_of_files)):
        newliste = get_list_of_words(liste_of_files[i])
        for mot in liste_des_mots.copy():
            if mot not in newliste:
                liste_des_mots.remove(mot)
    print(liste_des_mots)

    for mot in mots_non_importants:
        if mot in liste_des_mots:
            liste_des_mots.remove(mot)
    return liste_des_mots


def premier_president_ayant_parle_de(mots: list) -> str:
    ordre_chrono = ["Nomination_Giscard dEstaing.txt", "Nomination_Mitterrand1.txt", "Nomination_Mitterrand2.txt",
                    "Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Sarkozy.txt",
                    "Nomination_Hollande.txt", "Nomination_Macron.txt"]
    for file in ordre_chrono:
        liste_des_mots = get_list_of_words(file)
        for mot in mots:
            if mot in liste_des_mots:
                return extract_president_name(file)


if __name__ == "__main__":
    directory = "./cleaned/"
    # print(get_term_frequency("Nomination_Chirac1.txt"))
    # print(get_inverse_document_frequency("./cleaned"))
    # matrice, word_list = get_tf_id_matrix("./cleaned")
    # print(mots_importants(matrice, word_list))
    # liste_files = get_list_of_files_in_directory(directory)
    # print(extract_president_name(liste_files[0]))
    # mots_non_importants = mots_pas_importants(matrice, word_list)
    # print(mots_repetes_par(directory, "Chirac", mots_non_importants))
    # print(president_ayant_parle_de(directory, "nation"))
    # print(mots_repetes_par_tous_les_presidents(directory, mots_non_importants))
    #print(premier_president_ayant_parle_de(["climat", "écologie"]))
    matrice, liste_de_mots = get_tf_id_matrix(directory)
    mots_pas_importants = mots_pas_importants(matrice, liste_de_mots)
    print(mots_pas_importants)
    print(mots_repetes_par_tous_les_presidents(directory, mots_pas_importants))

