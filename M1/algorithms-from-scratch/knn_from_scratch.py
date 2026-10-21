# Section 1 : Imports de module
import P01_utils as utils
import math
import numpy as np
from scipy.spatial.distance import cdist

# Section 2 : Définition de fonctions

def dist(X_i, X_j):
    result = 0
    for i,j in zip(X_i,X_j):
        result+= (i-j)**2
    return math.sqrt(result)

def dist_numpy(X_i, X_j):
    cdist 

def kvoisins(test, train, k=5):
    test = test[0]
    train = train[0]
    result = []
    for i in range(len(test)):
        result.append([])
        for j in range(len(train)):
            result[i].append(dist(test[i], train[j]))
    return np.argsort(result)[:, :k]

def class_kvoisins(y):
    yF = y.count("F")
    yH = y.count("H")
    if yF > yH:
        return "F"
    elif yF < yH:
        return "H"

def k_plus_proches_voisins_liste(test, train, k=1):
    kv = kvoisins(test, train, k)
    liste = []
    result = []
    for i, val in enumerate(kv):
        liste.append([])
        for j in val:
            liste[i].append(train[1][j])
        result.append(class_kvoisins(liste[i]))
    return result

def k_plus_proches_voisins_numpy(test, train, k=1):
    distance = cdist(test[0],train[0])
    sort = np.argsort(distance)[:, :k]
    etiquette = train[1][sort]
    resultat = []
    for i in etiquette:
        if np.sum(i == 'H') > k/2:
            resultat.append('H')
        else:
            resultat.append('F')
    return resultat

# Section 3 : Tests de fonctions définies

dtrain = utils.lire_donnees(100)
dtest = utils.lire_donnees(10)

utils.visualiser_donnees(dtrain[0], dtrain[1], dtest[0])

print(dist(dtest[0][0],dtest[0][1]))
print(kvoisins(dtest, dtrain, 6))
print(class_kvoisins(dtrain))
print(k_plus_proches_voisins_liste(dtest, dtrain, 3))


dtrain_numpy = utils.lire_donnees_numpy(100)
dtest_numpy = utils.lire_donnees_numpy(10)

print(k_plus_proches_voisins_numpy(dtest_numpy,dtrain_numpy,5))