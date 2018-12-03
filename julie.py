import random

#Fonction pour trouver des voisins
#X est un vecteur représentant la position des 1
#nbNeighbour est le nombre de voisins qu'on veut créer
#Return une list de nouveaux voisins (sans doublon et ne comprenant pas le X de départ)
def findNeighbours(X, nbNeighbour):
  neighbours = []
  for i in range(0, nbNeighbour):
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
          if nb[j] != data[j]:
            doublon = False
        if doublon == True:
          found = True

      if not found:
        neighbours.append(newNeighbour)
        break
  return neighbours
