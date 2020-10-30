from graphes import *
import sys

# Fonction qui permet de choisir le graphe à étudier

def choose_graph():
    loop = True

    while loop:
        print("Entrez le numéro du graphe que vous voulez traiter")
        choix  = input("> ")
        print("Chargement du fichier '" + str(choix) + ".txt'.")

# Fonction qui lit les informations du graphe en .txt et les retourne

def read_graph(fileName = str):
    with open (fileName) as f:
        content = f.readlines()
        content = list(map(lambda s: s.strip(), content))
    
    if len(content) <= 2:
        content = None
        raise Exception(" > ERREUR ! Fichier trop petit.")

    try:
        content[0] = int(content[0])
    except ValueError as e:
        content = None
        print(" > Impossible de lire le nombre de sommets !")
        print(" > Error : " + str(e))
    
    try:
        content[1] = int(content[1])
    except ValueError as e:
        content = None
        print(" > Impossible de lire le nombre d'arcs !")
        print(" > Error : " + str(e))

    transitions = []
    for i in range(2, len(content)):
        print(content[i])
        transitions.append(content[i])
        
    return content, transitions

# Fonction qui crée l'objet Graphe que l'on va pouvoir manipuler ensuite

def load_graph(fileName = str):
    try:
        content, transitions = read_graph(fileName)
    except Exception as e:
        print("Erreur lors de la lecture du fichier")
        print(e)
        return None

    graphe = Graphe()
    graphe.set_nbSommets(content[0])
    graphe.set_nbArcs(content[1])
    graphe.add_arcs(transitions)

    return graphe
    