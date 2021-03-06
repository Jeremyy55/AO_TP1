import random

# Fonction pour trouver des voisins
# X est un vecteur représentant la position des 1
# nbNeighbour est le nombre de voisins qu'on veut créer
# Return une list de nouveaux voisins (sans doublon et ne comprenant pas le X de départ)


def find_neighbour(x):
    new_neighbour = x.copy()
    possible_element = [i for i in range(len(x))]
    row1 = possible_element.pop(random.randint(0, len(possible_element)-1))
    row2 = possible_element.pop(random.randint(0, len(possible_element)-1))
    new_neighbour[row1] = x[row2]
    new_neighbour[row2] = x[row1]
    return new_neighbour


def findNeighbours(X, nbNeighbour):
    neighbours = []
    for i in range(nbNeighbour):
        newNeighbour = X.copy()
        while True:
            row1 = int(round(random.random()*len(X))) % len(X)
            row2 = int(round(random.random()*len(X))) % len(X)
            tmp = newNeighbour[row1]
            newNeighbour[row1] = newNeighbour[row2]
            newNeighbour[row2] = tmp

            found = False
            for nb in neighbours:
                doublon = True
                for j in range(0, len(X)):
                    if nb[j] != newNeighbour[j]:
                        doublon = False
                if doublon == True:
                    found = True

            if not found:
                neighbours.append(newNeighbour)
                break
    return neighbours


def findNeighboursA(X, nbNeighbour, nPermut):
    neighbours = []
    for i in range(0, nbNeighbour):
        newNeighbour = X.copy()

        while True:

            permut_rows = random.sample(X, nPermut)

            temps = [newNeighbour[row] for row in permut_rows]

            for tmp, row in zip(reversed(temps), permut_rows):
                newNeighbour[row] = tmp

            found = False
            for nb in neighbours:
                doublon = True
                for j in range(0, len(X)):
                    if nb[j] != newNeighbour[j]:
                        doublon = False
                if doublon == True:
                    found = True

            if not found:
                neighbours.append(newNeighbour)
                break

    return neighbours
