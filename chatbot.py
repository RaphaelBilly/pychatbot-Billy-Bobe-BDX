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
print(files_names)

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
    print(liste_nom_president)
    return liste_nom_president

#print(extraire_nom(files_names))

def association_nom_prenom(nom_president):
    noms_prenoms = {"Chirac" : "Jacques",
                "Giscard dEstaing" : "Valery",
                "Hollande" : "François",
                "Macron" : "Emmanuel",
                "Mitterrand" : "François",
                "Sarkozy" : "Nicolas"}

    prenom = noms_prenoms[nom_president]
    return prenom
#print(association_nom_prenom("Chirac"))










