import string

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
        self.arcs = arcs

    def afficher(self):
        print("Nombre de sommets : " + int(self.nbSommets))
        print("Nombre d'arcs : " + int(self.nbArcs))
        print("Arcs : " + int(self.arcs))
