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
    for file in files_names:
        fichier = open("./speeches/" + file, "r")
        lignes = fichier.readlines()
        fichier_cleaned = open("./cleaned/" + file, "w")
        for ligne in lignes :
            ligne = ligne.replace("\n", " ")
            for i in range(len(ligne)):
                if ligne[i] in ".?!:;,()[]{}'-" and ligne[i - 1].isalpha() and ligne[i + 1].isalpha():
                    ligne = ligne.replace(ligne[i], " ")
                elif ligne[i] in ".?!:;,()[]{}'-" and ligne[i - 1].isalpha() and ligne[i + 1] == " ":
                    ligne = ligne.replace(ligne[i], " ")
                elif ligne[i] in ".?!:;,()[]{}'-":
                    ligne = ligne.replace(ligne[i], " ")
            for i in range(len(ligne)):
                if ligne[i] == " " and ligne[i + 1] == " ":
                    ligne = ligne.replace(ligne[i], "")
            fichier_cleaned.write(ligne)
        fichier.close()
        fichier_cleaned.close()
clean_punctuation()


def lower_case():
    for file in files_names:
        fichier = open("./cleaned/" + file, "r", encoding="utf-8")
        lignes = fichier.readlines()
        fichier_lower = open("./cleaned/" + file, "w", encoding="utf-8")
        for ligne in lignes:
            ligne = ligne.lower()
            fichier_lower.write(ligne)
        fichier.close()
        fichier_lower.close()
lower_case()

# fait une fonction qui ne laisse qu'un espace entre les mots et faire attention car parfois il peut y avoir plus de deux espaces collés



























