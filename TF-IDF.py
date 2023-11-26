from math import log10
import os
from chatbot import list_of_files
def TF_calculator(chaine_de_caractere):
    tableau = chaine_de_caractere.split(" ")
    dic = {}
    for element in tableau:
        if element not in dic.keys():
            dic[element] = 1
        else:
            dic[element] += 1
    return dic

def list_of_words(file):
    liste = []
    fichier = open(".speeches/" + file, "r")
    lines = fichier.readlines()
    for line in lines :
        line = line.split(" ")
        for word in line :
            if word not in liste :
                liste.append(word)
def IDF_calculator(directory):
    dic = {}
    files_names = list_of_files((directory, ".txt"))
    number_of_files = len(files_names)
    for file in files_names :
        list_of_words = list_of_words(file)
        for word in list_of_words :
            if word not in dic.keys() :
                dic[word] = 1
            else :
                dic[word] += 1
    for key in dic.keys() :
        value = dic[key]
        ratio = number_of_files/value
        dic [key] = log10(ratio)
    return dic


if __name__ == "__main__":
    print(TF_calculator(
        "il est au minimum nécessaire d’avoir  au qui le le au qui une fonction qui calcule le nombre d’occurrence de chaque mot dans un texte"))
    directory = "./speeches"