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
    for i in range(len(files_names)):
        digit = False
        files_names[i]= files_names[i][11:]
        for j in files_names[i]:
            if j.isdigit():
                digit = True
        if digit == True:
            files_names[i] = files_names[i][:-5]
        else :
            files_names[i] = files_names[i][:-4]
    for i in range (len(files_names)):
        if files_names[i] not in liste_nom_president:
            liste_nom_president.append(files_names[i])
    return liste_nom_president

#print(extraire_nom(files_names))

def association_nom_prenom(liste_nom_president):
    noms_prenoms = {"Chirac" : "Jacques",
                "Giscard dEstaing" : "Valery",
                "Hollande" : "François",
                "Macron" : "Emmanuel",
                "Mitterrand" : "François",
                "Sarkozy" : "Nicolas"}

    Liste_nom_prenom = []
    for name in liste_nom_president:
        Liste_nom_prenom.append(noms_prenoms[name] + " " + name)
    return Liste_nom_prenom

#print(association_nom_prenom(extraire_nom(files_names)))


cleaned_directory = os.path.join(os.path.dirname(directory), "cleaned")
os.makedirs(cleaned_directory, exist_ok=True)

def clean_punctuation():
    for file in files_names:
        fichier = open("./speeches/" + file, "r")
        # lire le fichier ligne par ligne
        lignes = fichier.readlines()
        # boucler pour chaque ligne
        #for line in lignes:

clean_punctuation()










