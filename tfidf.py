import math
from common import get_list_of_files_in_directory
from basic_functions import *

def get_list_of_words(file: str) -> list:
    file = open("./cleaned/" + file, "r", encoding="utf-8")
    list_of_words = list(set(file.read().split(" ")[:-1]))
    if '' in list_of_words:
        list_of_words.remove('')
    return list_of_words


def get_term_frequency(file: str) -> dict:
    term_frequency = {}
    fileLines = open("./cleaned/" + file, "r", encoding="utf-8").read().split(" ")
    if '' in fileLines:
        fileLines.remove('')
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
    liste_totale = []
    for i in range(len(files_names)):
        liste = get_list_of_words(files_names[i])
        allWords += liste
        liste_totale.append(liste)
    allWords = list(set(allWords))
    for word in allWords:
        for texte in liste_totale:
            if word in texte:
                if word not in document_frequency.keys():
                    document_frequency[word] = 1
                else:
                    document_frequency[word] += 1
    inverse_document_frequency = {}
    for word in document_frequency.keys():
        inverse_document_frequency[word] = math.log10(corpus_size / document_frequency[word])
    return inverse_document_frequency


def get_tf_id_matrix(directory: str) -> tuple:
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
    liste_des_presidents = {}
    for file in liste_of_files:
        liste_des_mots = get_list_of_words(file)
        if mot in liste_des_mots:
            nom_president = extract_president_name(file)
            if nom_president not in liste_des_presidents.keys():
                liste_des_presidents[nom_president] = 0
            liste_des_presidents[nom_president] += 1
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


def get_tf_id_matrix2(matrix: list) -> list:
    newMatrix = []
    for i in range(len(matrix[0])):
        newLine = []
        for j in range(len(matrix)):
            newLine.append(matrix[j][i])
        newMatrix.append(newLine)
    return newMatrix


def get_question_tf_score(question: list) -> dict:
    tf_scores = {}
    for word in question:
        if word not in tf_scores.keys():
            tf_scores[word] = 0
        tf_scores[word] += 1
    return tf_scores


def get_tf_id_vector(question: list, list_of_words: list, directory: str) -> list:
    idf_score = get_inverse_document_frequency(directory)
    question_tf_score = get_question_tf_score(question)
    tf_id_scores = []
    for word in list_of_words:
        if word in question:
            tf_score = question_tf_score[word]
            tf_id_score = tf_score * idf_score[word]
        else:
            tf_id_score = 0
        tf_id_scores.append(tf_id_score)
    return tf_id_scores


def get_scalar_product(vector1: list, vector2: list) -> float:
    sum = 0
    for i in range(len(vector1)):
        value = vector1[i] * vector2[i]
        sum += value
    return sum


def get_vector_norm(vector: list) -> float:
    norm = 0
    for i in range(len(vector)):
        value = vector[i] ** 2
        norm += value
    norm = math.sqrt(norm)
    return norm


def get_similarity(vector1: list, vector2: list) -> float:
    scalar_product = get_scalar_product(vector1, vector2)
    norm1 = get_vector_norm(vector1)
    norm2 = get_vector_norm(vector2)
    return scalar_product / (norm1 * norm2)

def get_most_relevant_document(matrice: list,question_vector: list,directory:str) -> str:
    liste_of_files = get_list_of_files_in_directory(directory)
    liste_des_scores = []
    for i in range(len(matrice)):
        liste_des_scores.append(get_similarity(matrice[i],question_vector))
    max = 0
    indice = 0
    for _ in range(len(liste_des_scores)):
        if liste_des_scores[_]>= max :
            max = liste_des_scores[_]
            indice = _
    return liste_of_files[indice]


def get_most_revelant_word(vector : list, list_of_words : list) -> str :
    max = 0
    mot = ""
    for i in range (len(vector)):
        if vector[i] >= max:
            max = vector[i]
            mot = list_of_words[i]
    return mot

def get_answer(word : str, file : str) -> str :
    lines = open("./speeches/" + file, "r", encoding="utf-8").readlines()
    for i in range(len(lines)):
        lines[i] = clean_text(lines[i])
        lines[i] = lines[i].split(" ")
    for line in lines :
        if word in line:
            answer = ""
            for element in line:
                answer += element + ' '
            answer = (answer[:-1])
            return answer

def get_refined_answer(tokenised_question, answer):
    question_starters = {
        "comment": "Après analyse, ",
        "pourquoi": "Car, ",
        "peux tu": "Oui, bien sûr"
    }
    if answer == "None" :
        return("Je ne suis pas en mesure de répondre à cette question...")
    for i in tokenised_question:
        if i in question_starters.keys():
            return (question_starters[i] + answer[:-1] + '.')
    answer = answer[0].upper() + answer[1:]
    return answer


if __name__ == "__main__":
    directory = "./cleaned/"

