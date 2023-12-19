from tfidf import *
from common import get_list_of_files_in_directory
from basic_functions import *


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

    choice = -1
    while choice < 0 or choice > 5 :
        choice = int(input("Entrer votre choix [1-5]: "))

    directory = "./cleaned/"
    matrice, liste_de_mots = get_tf_id_matrix(directory)
    match choice:
         case 1:
             print("Tu as choisi 1")
             mots = mots_pas_importants(matrice, liste_de_mots)
             for mot in mots :
                 print(mot, end = ", ")
             print("sont les mots dits non-importants du corpus.")
         case 2:
             print("Tu as choisi 2")
             mot = mots_importants(matrice, liste_de_mots)[0]
             print("Le mot le plus important du corpus est : " + mot + ".")
         case 3:
             print("Tu as choisi 3")
             president = input("Ecris le nom du président: ")
             liste = mots_repetes_par(directory, president, mots_pas_importants(matrice, liste_de_mots))
             if len(liste) == 1:
                print("Le mot que M." + president + " a le plus répété est : " + liste[0] + ".")
             else :
                for i in range(len(liste)):
                    if i == len(liste) -1:
                        print(liste[i], end = " ")
                    else :
                        print(liste[i], end = " ")
                print("sont les mots que M." + president + "a répété le plus de fois.")
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
            president = premier_president_ayant_parle_de(L)
            if len(L) == 1 :
                print("Le premier président ayant parlé de '" + mot + "' est " + president + "." )
            else :
                print("Le premier président ayant parlé de", end = " ")
                for i in range(len(L)):
                    if i == len(L) -1:
                        print("'" + L[i] + "'", end = " ")
                    else :
                        print("'" + L[i] + "' ou de", end = " ")
                print("est M." + president + "." )


elif choix ==2 :
    directory="./cleaned"
    question = input("Quelle est votre question ?")
    question = get_question_tokenised(question)
    question_in_corpus = get_questions_words_in_corpus(question)
    matrice, liste_de_mots = get_tf_id_matrix(directory)
    matrice = get_tf_id_matrix2(matrice)
    vector = get_tf_id_vector(question_in_corpus, liste_de_mots, directory)
    mot = get_most_revelant_word(vector, liste_de_mots)
    document = get_most_relevant_document(matrice, vector, directory)
    answer = get_answer(mot, document)

    print(get_refined_answer(question, answer))

