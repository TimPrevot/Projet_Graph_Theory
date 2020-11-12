from graphe import *
from fonctions import *

if __name__ == "__main__":
    loop = True
    while loop:
        file = choose_graph()
        graphe = Graphe()
        graphe.define_graph(file)
        graphe.get_arcs(file)
        graphe.afficher()
        print()
        graphe.init_dist()
        print()
        print("Floyd-Warshall :")
        graphe.floyd_warshall()
        print()
        print("Détection des circuits absorbants :")
        print()
        graphe.detectionCircuitAbsorbant()
        print("Voulez-vous choisir un autre graphe ? Tapez Oui ou Non")
        yesNo = input()
        yesNo = yesNo.upper()
        if yesNo == "NON":
            loop = False
