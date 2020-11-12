from graphe import *

# Fonction qui permet de choisir le graphe à étudier

def choose_graph():
    notAnInt = True
    while notAnInt:
        try:
            print("Entrez le numéro du graphe que vous voulez traiter")
            choix = int(input("> "))
            notAnInt = False
        except ValueError:
            print("Veuillez indiquer un entier")
    print("Chargement du fichier 'L3-G7-graphe" + str(choix) + ".txt'.")
    return "GraphesDeTest\L3-G7-graphe" + str(choix) + ".txt"
