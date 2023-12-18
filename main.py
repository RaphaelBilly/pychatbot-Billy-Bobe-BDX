import os
from common import get_list_of_files_in_directory
from basic_functions import *
from tfidf import *


files_names = get_list_of_files_in_directory("./speeches")
get_cleaned_speeches(files_names)


print("Menu :")
print("1. Souhaitez vous accéder aux fonctionnalités prédéfénies du menu ?")
print("2. Souhaitez vous poser une question ?")
choix = int(input("Entrer votre choix [1-2]: "))
if choix == 1:
    print("Menu :")
    print("1. Afficher la liste des mots les moins importants dans le corpus de documents.")
    print("2. Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé")
    print("3. Indiquer le(s) mot(s) le(s) plus répété(s) par le président souhaité")
    print("4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé du mot de votre choix et celui qui l’a répété le plus de fois")
    print("5. Indiquer le premier président à parler du/des mot/s de votre choix (exemple : écologie / climat)")
    print("6. Indiquer hormis les mots dits « non importants », quel(s) est(sont) le(s) mot(s) que tous les présidents ont évoqués")

    choice = -1
    while choice < 0 or choice > 6 :
        choice = int(input("Entrer votre choix [1-6]: "))

    directory = "./cleaned/"
    matrice, liste_de_mots = get_tf_id_matrix(directory)
    match choice:
         case 1:
             print("Tu as choisi 1")
             print(mots_pas_importants(matrice, liste_de_mots))
         case 2:
             print("Tu as choisi 2")
             print(mots_importants(matrice, liste_de_mots))
         case 3:
             print("Tu as choisi 3")
             president = input("Ecris le nom du président: ")
             print(mots_repetes_par(directory, president, mots_pas_importants(matrice, liste_de_mots)))
         case 4:
             print("Tu as choisi 4")
             mot = input("Ecris le mot: ")
             print(president_ayant_parle_de(directory, mot))
         case 5:
            print("Tu as choisi 5")
            L = []
            n = -1
            while n <= 0:
                n = int(input("Combien de mots souhaitez vous afin d'indiquer le premier président à parler du/des mot/s de votre choix ? : "))
            for i in range(n):
                mot = input("Entrez le " + str(i + 1) + " mot :")
                L.append(mot)
            print(premier_president_ayant_parle_de(L))

         case 6:
             print("You chose 6")

elif choix ==2 :
    user_question = input("Quelle est votre question ?")

    #print(get_question_tokenised(user_question))
    # test : print(get_questions_words_in_corpus(get_question_tokenised("Quel est le président qui a le plus parlé de l'écologie ?")))
