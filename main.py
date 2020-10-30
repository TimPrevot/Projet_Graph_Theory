from graphes import *
from fonctions import *


if __name__ == "__main__":
    graphe = load_graph("graph_test.txt")
    graphe.afficher()
    print()
    graphe.create_matrix_adja()
    graphe.create_matrix_val()
    print()
    print()
    graphe.find_start_end()
    graphe.find_values()
    print()
    graphe.fill_matrix_adja()
    graphe.fill_matrix_val()
    graphe.afficher()

    