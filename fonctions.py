from graphes import *

def choose_graph():
    loop = True

    while loop:
        print("Entrez le numéro du graphe que vous voulez traiter")
        choix  = input("> ")
        print("Chargement du fichier '" + str(choix) + ".txt'.")

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
        transitions.append((int(content[i][0]), int(content[i][1]), int(content[i][2])))
        
    return content, transitions

def load_graph(fileName = "graph_test.txt"):
    try:
        content, transitions = read_graph(fileName)
    except Exception as e:
        print("Erreur lors de la lecture du fichier")
        print(e)
        return None

    graphe = Graphe()
    