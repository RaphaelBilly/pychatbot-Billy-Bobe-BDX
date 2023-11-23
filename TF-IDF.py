from math import log10
import os
def TF_calculator(chaine_de_caractere):
    tableau = chaine_de_caractere.split(" ")
    dic = {}
    for element in tableau:
        if element not in dic.keys():
            dic[element] = 1
        else:
            dic[element] += 1
    return dic


def IDF_calculator(directory):
    dic = {}
    for files in directory :
        pass

if __name__ == "__main__":
    print(TF_calculator(
        "il est au minimum nécessaire d’avoir  au qui le le au qui une fonction qui calcule le nombre d’occurrence de chaque mot dans un texte"))
    directory = "./speeches"