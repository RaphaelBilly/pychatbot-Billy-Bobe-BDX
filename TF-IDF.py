from math import log10
import os


def get_list_of_files_in_directory(directory: str) -> list:
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith("txt"):
            files_names.append(filename)
    return files_names


def list_of_words(file):
    liste = []
    fichier = open("./cleaned/" + file , "r")
    lines = fichier.readlines()
    for line in lines:
        line = line.split(" ")
        for word in line:
            if word not in liste:
                liste.append(word)
    return liste


def TF_calculator(file):
    dic = {}
    fichier = open("./cleaned/" + file, "r")
    lines = fichier.readlines()
    for line in lines:
        line = line.split(" ")
        for word in line :
            if word not in dic.keys():
                dic[word] = 1
            else:
                dic[word] += 1
    liste = list_of_words(file)
    for word in liste:
        dic[word] = dic[word] / len(liste)
    return dic


def IDF_calculator(directory):
    dic = {}
    files_names = get_list_of_files_in_directory(directory)
    number_of_files = len(files_names)
    for file in files_names:
        list_of_all_words = list_of_words(file)
        for word in list_of_all_words:
            if word not in dic.keys():
                dic[word] = 1
            else:
                dic[word] += 1
    for key in dic.keys():
        value = dic[key]
        ratio = number_of_files / value
        dic[key] = log10(ratio)
    return dic


def TF_IDF_calculator(directory):
    files_names = get_list_of_files_in_directory(directory)
    matrice = []
    IDF_scores = IDF_calculator(directory)
    list_of_all_words = IDF_scores.keys()
    final_list = []
    for word in list_of_all_words:
        final_list.append(word)
        word_TFIDF_scores = []
        for file in files_names:
            if word in list_of_words(file):
                TF_scores = TF_calculator(file)
                word_TF_score = TF_scores[word]
            else :
                word_TF_score = 0
            word_IDF_score = IDF_scores[word]
            word_TFIDF_score = word_TF_score * word_IDF_score
            word_TFIDF_scores.append(word_TFIDF_score)
        matrice.append(word_TFIDF_scores)
    return matrice, final_list


if __name__ == "__main__":
    pass

