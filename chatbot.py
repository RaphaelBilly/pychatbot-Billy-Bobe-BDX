import os

#Récupère les noms des fichiers contenants les discours
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

directory = "./speeches"
files_names = list_of_files(directory, "txt")

def extraire_nom(files_names):
    liste_nom_president = []
    #boucle for parcourant la liste des noms de fichiers
    for i in range(len(files_names)):
        digit = False
        files_names[i]= files_names[i][11:]                 #on enlève le début du nom de fichier
        for j in files_names[i]:                            #on vérifie si il y a un chiffre dans le nom de fichier
            if j.isdigit():
                digit = True
        if digit == True:                                   #si il y a un chiffre, on enlève les 5 derniers caractères
            files_names[i] = files_names[i][:-5]
        else :                                              #sinon on enlève les 4 derniers caractères
            files_names[i] = files_names[i][:-4]
    for i in range (len(files_names)):                      #on enlève les doublons
        if files_names[i] not in liste_nom_president:
            liste_nom_president.append(files_names[i])
    return liste_nom_president

#print(extraire_nom(files_names))

def association_nom_prenom(liste_nom_president):          #on associe les noms de famille aux prénoms
    noms_prenoms = {"Chirac" : "Jacques",
                "Giscard dEstaing" : "Valery",
                "Hollande" : "François",
                "Macron" : "Emmanuel",
                "Mitterrand" : "François",
                "Sarkozy" : "Nicolas"}                    #dictionnaire associant les noms de famille aux prénoms

    Liste_nom_prenom = []
    for name in liste_nom_president:                      #on associe les noms de famille aux prénoms
        Liste_nom_prenom.append(noms_prenoms[name] + " " + name)
    return Liste_nom_prenom

#print(association_nom_prenom(extraire_nom(files_names)))


cleaned_directory = os.path.join(os.path.dirname(directory), "cleaned") #création du dossier cleaned
os.makedirs(cleaned_directory, exist_ok=True)

def clean_punctuation():
    for file in files_names:                                        #boucle for parcourant la liste des noms de fichiers
        fichier = open("./speeches/" + file, "r")                   #ouverture des fichiers en lecture du dossier speeches
        lignes = fichier.readlines()                                #création d'une liste contenant les lignes du fichier
        fichier_cleaned = open("./cleaned/" + file, "w")            #création des fichiers dans le dossier cleaned en écriture
        for ligne in lignes :                                       #boucle for parcourant les lignes du fichier
            for i in range(len(ligne)):                             #boucle for parcourant les caractères de la ligne
                if ligne[i] in ".?!:;,()[]{}'-":                    #si le caractère est un signe de ponctuation
                    ligne = ligne.replace(ligne[i], " ")            #on le remplace par un espace
            fichier_cleaned.write(ligne)                            #on écrit la ligne dans le fichier
        fichier.close()                                             #fermeture des fichiers
        fichier_cleaned.close()

        #CODE DE LA FONCTION A AMELIORER CAR ELLE MET 2 ESPACES A LA SUITE SI UNE VIRGULE EST SUPPRIMEE OU ENCORE
        # Faire attention en corrigeant le problème du commentaire ci dessus à ne pas concaténer par exemple elle-même en ellemême




clean_punctuation()































