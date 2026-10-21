# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import csv
import graphs
import armining

__author__ = 'Mathieu Ben, Romain Tavenard'

def read_grades_from_csv(path):
    grades = {}
    missing_grades = []
    with open(path, 'r') as inFile:
        csv_reader = csv.reader(inFile)
        first_line = next(csv_reader)
        items = first_line[1:]
        for line in csv_reader:
            user = line[0]
            for i,grade in enumerate(line[1:]):
                if grade != '':
                    grades[(user, items[i])] = float(grade)
                else:
                    missing_grades.append((user, items[i]))
    return grades, missing_grades

### Prog. principal

## Scénario 1

##1.
g = nx.read_edgelist('data/mathInfoGraph.txt')
# print(g.nodes())
# plt.figure()
# nx.draw_networkx(g)
# plt.show()

##2.
notes = read_grades_from_csv('data/notes.csv')
# print(notes[0])
# print(notes[1])

##3.
scores_dict = {}
# for (utilisateur, produit), note in notes[0].items():
#     if utilisateur not in scores_dict:
#         scores_dict[utilisateur] = {}
#     scores_dict[utilisateur][produit] = note
# print(scores_dict)

# for cible in notes[1]:
    # On appelle la fonction en passant le dictionnaire structuré et le tuple cible
    # Essaie de spécifier la fonction ou de restreindre si le prof l'a prévu
    # note_estimee = graphs.collaborative_filtering(scores=notes[0], target=cible)
    # print(note_estimee)

for (target_user, target_item) in notes[1]:
    predict = graphs.user_based_collaborative_filtering(notes[0], (target_user, target_item), graph=g)
    print(f"{(target_user, target_item)} --> {predict:.2f}")
    if predict>12:
        print(f'Nous recommandons le produit {target_item} à l\'utilisateur {target_user}')