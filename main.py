from common import get_list_of_files_in_directory
from basic_functions import *
from tfidf import *


files_names = get_list_of_files_in_directory("./speeches")
get_cleaned_speeches(files_names)

print("Menu :")
print("1. Afficher la liste des mots les moins importants dans le corpus de documents.")
print("2. Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé")
print("3. Indiquer le(s) mot(s) le(s) plus répété(s) par le président souhaité")
print("4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé du mot de votre choix et celui qui l’a répété le plus de fois")
print("5. Indiquer le premier président à parler du/des mot/s de votre choix")
print("6. Indiquer hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués")

choice = -1
while choice < 0 or choice > 6 :
    choice = int(input("Enter your choice [1-6]: "))

directory = "./cleaned/"
matrice, liste_de_mots = get_tf_id_matrix(directory)
match choice:
     case 1:
         print("You chose 1")
         print(mots_pas_importants(matrice, liste_de_mots))
     case 2:
         print("You chose 2")
         print(mots_importants(matrice, liste_de_mots))
     case 3:
         print("You chose 3")
         president = input("Enter the name of the president: ")
         print(mots_repetes_par(directory, president))
     case 4:
         print("You chose 4")
         mot = input("Enter the word: ")
         print(president_ayant_parle_de(directory, mot))
     case 5:
         print("You chose 5")

     case 6:
         print("You chose 6")
