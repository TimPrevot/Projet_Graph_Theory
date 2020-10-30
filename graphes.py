import string

# Définition de la classe Graphe() utilisée tout au long du programme pour représenter nos graphes

class Graphe:
    def __init__(self):
        self.nbSommets = 0
        self.nbArcs = 0
        self.arcs = []

    def set_nbSommets(self, nbSommets : int):
        self.nbSommets = nbSommets
    
    def set_nbArcs(self, nbArcs : int):
        self.nbArcs = nbArcs

    def add_arcs(self, arcs : list):
        for i in range (0, len(arcs)):
            self.arcs.append(arcs[i])

    def afficher(self):
        print("Nombre de sommets : " + str(self.nbSommets))
        print("Nombre d'arcs : " + str(self.nbArcs))
        print("Arcs : " + str(self.arcs))
