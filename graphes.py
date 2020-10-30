import string

# Définition de la classe Graphe() utilisée tout au long du programme pour représenter nos graphes

class Graphe:
    def __init__(self):
        self.nbSommets = 0
        self.nbArcs = 0
        self.arcs = []
        self.matrix = []
        self.arcsStart = []
        self.arcsEnd = []

    def set_nbSommets(self, nbSommets : int):
        self.nbSommets = nbSommets
    
    def set_nbArcs(self, nbArcs : int):
        self.nbArcs = nbArcs

    def add_arcs(self, arcs : list):
        for i in range (0, len(arcs)):
            self.arcs.append(arcs[i])

    def afficher_matrix(self):
        print("Matrice d'adjacence : ")
        for i in range (0, self.nbSommets):
            print(self.matrix[i])

    def afficher(self):
        print("Nombre de sommets : " + str(self.nbSommets))
        print("Nombre d'arcs : " + str(self.nbArcs))
        print("Arcs : " + str(self.arcs))
        if (self.matrix != []):
            self.afficher_matrix()

    # Méthode qui crée la matrice d'adjacence du graphe et la remplit de 0

    def create_matrix(self):
        for i in range(0, self.nbSommets):
            self.matrix.append([])
            for j in range(0, self.nbSommets):
                self.matrix[i].append(0)

    # Méthode qui remplit la matrice d'adjacence en fonction des arcs du graphe

    def fill_matrix(self):
        for i in range(0, len(self.arcsStart)):
            self.matrix[self.arcsStart[i]][self.arcsEnd[i]] = 1
            self.matrix[self.arcsEnd[i]][self.arcsStart[i]] = 1
    
    # Méthode qui détermine les sommets d'où partent et / ou arrivent les arcs

    def find_start_end(self):
        for i in range(0, len(self.arcs)):
            self.arcsStart.append(int(self.arcs[i][0]))
            self.arcsEnd.append(int(self.arcs[i][2]))