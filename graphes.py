import string

# Définition de la classe Graphe() utilisée tout au long du programme pour représenter nos graphes

class Graphe:
    def __init__(self):
        self.nbSommets = 0
        self.nbArcs = 0
        self.arcs = []
        self.matrix_adja = []
        self.matrix_val =[]
        self.arcsStart = []
        self.arcsEnd = []
        self.arcsValues = []

    def set_nbSommets(self, nbSommets : int):
        self.nbSommets = nbSommets
    
    def set_nbArcs(self, nbArcs : int):
        self.nbArcs = nbArcs

    def add_arcs(self, arcs : list):
        for i in range (0, len(arcs)):
            self.arcs.append(arcs[i])

    def afficher_matrix_adja(self):
        print("Matrice d'adjacence : ")
        for i in range (0, self.nbSommets):
            print(self.matrix_adja[i])

    def afficher_matrix_val(self):
        print("Matrice de valeurs : ")
        for i in range (0, self.nbSommets):
            print(self.matrix_val[i])  

    def afficher(self):
        print("Nombre de sommets : " + str(self.nbSommets))
        print("Nombre d'arcs : " + str(self.nbArcs))
        print("Arcs : " + str(self.arcs))
        if (self.matrix_adja != []):
            self.afficher_matrix_adja()
        if (self.matrix_val != []):
            self.afficher_matrix_val()

    # Méthode qui crée la matrice d'adjacence du graphe et la remplit de 0

    def create_matrix_adja(self):
        for i in range(0, self.nbSommets):
            self.matrix_adja.append([])
            for j in range(0, self.nbSommets):
                self.matrix_adja[i].append(0)

    # Méthode qui crée la matrice de valeurs du graphe et la remplit de 0

    def create_matrix_val(self):
        for i in range(0, self.nbSommets):
            self.matrix_val.append([])
            for j in range(0, self.nbSommets):
                self.matrix_val[i].append(0)

    # Méthode qui remplit la matrice d'adjacence en fonction des arcs du graphe

    def fill_matrix_adja(self):
        for i in range(0, len(self.arcsStart)):
            self.matrix_adja[self.arcsStart[i]][self.arcsEnd[i]] = 1
            self.matrix_adja[self.arcsEnd[i]][self.arcsStart[i]] = 1

    # Méthode qui remplit la matrice de valeurs en fonction des arcs du graphe

    def fill_matrix_val(self):
        for i in range(0, len(self.arcsValues)):
            self.matrix_val[self.arcsStart[i]][self.arcsEnd[i]] = self.arcsValues[i]
            self.matrix_val[self.arcsEnd[i]][self.arcsStart[i]] = self.arcsValues[i]

    
    # Méthode qui détermine les sommets d'où partent et / ou arrivent les arcs

    def find_start_end(self):
        for i in range(0, len(self.arcs)):
            self.arcsStart.append(int(self.arcs[i][0]))
            self.arcsEnd.append(int(self.arcs[i][2]))

    # Méthode qui récupère les valeurs des différents arcs et les range dans un tableau

    def find_values(self):
        for i in range(0, len(self.arcs)):
            self.arcsValues.append(int(self.arcs[i][4]))