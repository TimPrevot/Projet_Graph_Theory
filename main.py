from graphes import *
from fonctions import *


if __name__ == "__main__":
    graphe = load_graph("graph_test.txt")
    graphe.afficher()
    print()
    graphe.create_matrix()
    print()
    print()
    graphe.find_start_end()
    print()
    graphe.fill_matrix()
    graphe.afficher()

    