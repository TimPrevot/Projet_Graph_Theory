# On fixe la valeur de INF à 99999
INF = 99999


# Définition de notre classe Graphe

class Graphe:
    def __init__(self):
        self.nbSommets = 0
        self.nbArcs = 0
        self.arcs = []
        self.matrix_val = []
        self.matrix_adja = []
        self.dist = []
        self.P = []
        self.circuitAbsorbant = False

    # Méthode qui lit le graphe et sauvegarde le nombre de sommets, d'arcs et la matrice de valeurs

    def define_graph(self, filename: str):
        currentLine = 0
        try:
            with open(filename, 'r') as file:
                for line in file:
                    currentLine += 1
                    if currentLine == 1:
                        self.nbSommets = int(line)

                        # Initialisation de la matrice de valeurs et de la matrice d'adjacence

                        self.matrix_val = [[None for i in range(self.nbSommets)] for j in range(self.nbSommets)]
                        self.matrix_adja = [[None for i in range(self.nbSommets)] for j in range(self.nbSommets)]
                    elif currentLine == 2:
                        self.nbArcs = int(line)
                    elif currentLine <= self.nbArcs + 2:
                        l = line.split(" ")

                        # Calcul de la matrice de valeurs

                        self.matrix_val[int(l[0])][int(l[1])] = int(l[2])

                        # On déduit la matrice d'adjacence à partir de la matrice de valeurs
                        # Si on détecte une valeur, on met un 1 dans la case correspondante de la matrice d'adjacence

                        if self.matrix_val[int(l[0])][int(l[1])] != None:
                            self.matrix_adja[int(l[0])][int(l[1])] = 1
        except Exception as e:
            print("Erreur lors de la lecture du fichier !")
            print(e)
            return None

    # Méthode pour afficher les différents attributs du graphe

    def afficher(self):
        print("Nombre de sommets : " + str(self.nbSommets))
        print("Nombre d'arcs : " + str(self.nbArcs))
        print("Arcs : " + str(self.arcs))
        if self.matrix_adja:
            print("Matrice d'adjacence :")
            self.afficher_matrix_adja()
        if self.matrix_val:
            print("Matrice de valeurs :")
            self.afficher_matrix_val()

    # Méthode qui récupère la liste des arcs du graphe et les place dans une liste

    def get_arcs(self, filename: str):
        with open(filename, 'r') as file:
            content = file.readlines()
            content = list(map(lambda s: s.strip(), content))
        transitions = []
        for i in range(2, len(content)):
            transitions.append(content[i])
        for i in range(0, len(transitions)):
            self.arcs.append(transitions[i])

    # Méthode pour afficher la matrice de valeurs du graphe

    def afficher_matrix_val(self):
        maxLength = 0

        # On recherche le nombre maximum de caractères à utiliser pour afficher une case de la matrice de valeurs

        for i in range(self.nbSommets):
            for j in range(self.nbSommets):
                if self.matrix_val[i][j] and len(str(self.matrix_val[i][j])) > maxLength:
                    maxLength = len(str(self.matrix_val[i][j]))

        # On affiche la première ligne ainsi qu'une barre horizontale en dessous

        print(' ' * (maxLength + 1), end="|")
        for i in range(self.nbSommets):
            print(str(i).rjust(maxLength + 1, ' '), end="")
        print()
        print("-" * ((maxLength + 1) * (self.nbSommets + 1) + 1))

        # On affiche les valeurs de la matrice

        for i in range(self.nbSommets):
            for j in range(self.nbSommets):
                if j == 0:
                    print(str(i).rjust((maxLength + 1), ' '), end="|")
                if self.matrix_val[i][j] != None:
                    print(str(self.matrix_val[i][j]).rjust((maxLength + 1), ' '), end="")
                else:
                    print(' ' * (maxLength + 1), end="")
            print()

    # Méthode pour afficher la matrice d'adjacence du graphe

    def afficher_matrix_adja(self):
        maxLength = 0

        # On recherche le nombre maximum de caractères à utiliser pour afficher une case de la matrice d'adjacence

        for i in range(self.nbSommets):
            for j in range(self.nbSommets):
                if self.matrix_adja[i][j] and len(str(self.matrix_adja[i][j])) > maxLength:
                    maxLength = len(str(self.matrix_adja[i][j]))

        # On affiche la première ligne ainsi qu'une barre horizontale en dessous

        print(' ' * (maxLength + 1), end="|")
        for i in range(self.nbSommets):
            print(str(i).rjust(maxLength + 1, ' '), end="")
        print()
        print("-" * ((maxLength + 1) * (self.nbSommets + 1) + 1))

        # On affiche les valeurs de la matrice

        for i in range(self.nbSommets):
            for j in range(self.nbSommets):
                if j == 0:
                    print(str(i).rjust((maxLength + 1), ' '), end="|")
                if self.matrix_adja[i][j] != None:
                    print(str(self.matrix_adja[i][j]).rjust((maxLength + 1), ' '), end="")
                else:
                    print(' ' * (maxLength + 1), end="")
            print()

    # Méthode qui initialise la matrice des distances minimales à partir de la matrice de valeurs

    def init_dist(self):
        self.dist = [[None] * self.nbSommets for i in range(self.nbSommets)]
        self.P = [[0] * self.nbSommets for i in range(self.nbSommets)]
        for i in range(self.nbSommets):
            for j in range(self.nbSommets):

                # Si la case correspondante dans la matrice de valeurs contient une valeur, on la recopie

                if self.matrix_val[i][j] != None:
                    self.dist[i][j] = self.matrix_val[i][j]

                # Sinon, la case prend la valeur INF que l'on a définie à 99999

                else:
                    self.dist[i][j] = INF

        # On remplit la diagonale de 0

        for i in range(self.nbSommets):
            self.dist[i][i] = 0
        for arc in self.arcs:
            el = arc.split(" ")

            # Si on détecte un arc qui boucle sur lui-même, on indique le poids dans la case correspondante

            if el[0] == el[1]:
                self.dist[int(el[0])][int(el[0])] = int(el[2])

        # On affiche la matrice des distances initialisée

        print("Matrice des distances minimales initiale :")
        self.afficher_dist()

    # Méthode pour afficher la matrice des distances minimales du graphe

    def afficher_dist(self):
        maxLength = 0

        # On recherche le nombre maximum de caractères à utiliser pour afficher une case de la matrice des distances

        for i in range(self.nbSommets):
            for j in range(self.nbSommets):
                if self.dist[i][j] and len(str(self.dist[i][j])) > maxLength:
                    maxLength = len(str(self.dist[i][j]))

        # On affiche la première ligne ainsi qu'une barre horizontale en dessous

        print(' ' * (maxLength + 1), end="|")
        for i in range(self.nbSommets):
            print(str(i).rjust(maxLength + 1, ' '), end="")
        print()
        print("-" * ((maxLength + 1) * (self.nbSommets + 1) + 1))

        # On affiche les valeurs de la matrice

        for i in range(self.nbSommets):
            for j in range(self.nbSommets):
                if j == 0:
                    print(str(i).rjust((maxLength + 1), ' '), end="|")
                if self.dist[i][j] != None:
                    print(str(self.dist[i][j]).rjust((maxLength + 1), ' '), end="")
                else:
                    print(' ' * (maxLength + 1), end="")
            print()

    # Méthode pour afficher la matrice des prédécésseurs du graphe

    def afficher_P(self):
        maxLength = 0

        # On recherche le nombre maximum de caractères à utiliser pour afficher une case de la matrice des prédécesseurs

        for i in range(self.nbSommets):
            for j in range(self.nbSommets):
                if self.P[i][j] and len(str(self.P[i][j])) > maxLength:
                    maxLength = len(str(self.P[i][j]))

        # On affiche la première ligne ainsi qu'une barre horizontale en dessous

        print(' ' * (maxLength + 1), end="|")
        for i in range(self.nbSommets):
            print(str(i).rjust(maxLength + 1, ' '), end="")
        print()
        print("-" * ((maxLength + 1) * (self.nbSommets + 1) + 1))

        # On affiche les valeurs de la matrice

        for i in range(self.nbSommets):
            for j in range(self.nbSommets):
                if j == 0:
                    print(str(i).rjust((maxLength + 1), ' '), end="|")
                if self.P[i][j] != None:
                    print(str(self.P[i][j]).rjust((maxLength + 1), ' '), end="")
                else:
                    print(' ' * (maxLength + 1), end="")
            print()

    # Méthode pour exécuter l'algorithme de Floyd-Warshall

    def floyd_warshall(self):

        # On initialise la matrice des prédécesseurs

        for arc in self.arcs:
            el = arc.split(" ")
            self.P[int(el[0]) - 1][int(el[1]) - 1] = int(el[1]) - 1

        # On exécute l'algorithme

        # k parcourt les sommets intermédiaires

        for k in range(self.nbSommets):
            print("k=", k)

            # On parcourt notre matrice de distances avec i et j

            for i in range(self.nbSommets):
                for j in range(self.nbSommets):
                    if self.dist[i][k] != INF and self.dist[k][j] != INF:

                        # Si on trouve un chemin moins lourd passant par k, alors on indique son poids dans dist

                        self.dist[i][j] = min(self.dist[i][j], self.dist[i][k] + self.dist[k][j])
                        if self.dist[i][j] > (self.dist[i][k] + self.dist[k][j]):
                            self.P[i][j] = self.P[k][j]

            # On affiche la matrice des distances et la matrice des prédécésseurs

            print("L=")
            self.afficher_dist()
            print("P=")
            self.afficher_P()

    # Méthode pour détecter la présence d'un circuit absorbant dans le graphe

    def detectionCircuitAbsorbant(self):

        # On parcourt notre graphe avec i et j

        for i in range(self.nbSommets):
            for j in range(self.nbSommets):

                # Si on détecte une valeur négative dans la matrice des distances, il y a un circuit absorbant

                if self.dist[i][j] < 0:
                    self.circuitAbsorbant = True
                else:
                    continue
        if self.circuitAbsorbant:
            print("Le graphe possède au moins un circuit absorbant.")
        else:
            print("Le graphe ne possède pas de circuit absorbant.")
