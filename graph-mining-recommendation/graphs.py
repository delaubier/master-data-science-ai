import networkx as nx
import math

__author__ = 'Romain Tavenard romain.tavenard[at]univ-rennes2.fr'


def sorted_dict(d):
    return sorted(d.items(), key=lambda t: t[1], reverse=True)


def top_k_triplets(triplets, k):
    return sorted(triplets, key=lambda t: t[2], reverse=True)[:k]


def pagerank(g, alpha=0.9, max_iter=100):
    n_nodes = len(g)
    pagerank_dict = {node: 1. / n_nodes for node in g.nodes()}
    for iter in range(max_iter):
        pagerank_dict_new = {node: (1. - alpha) / n_nodes for node in g.nodes()}
        for node_j in g.nodes():
            for node_i in g.predecessors(node_j):
                pagerank_dict_new[node_j] += alpha * (pagerank_dict[node_i] / g.out_degree(node_i))
        pagerank_dict = pagerank_dict_new.copy()
    return pagerank_dict


def cosine_sim(v1, v2):
    # TODO : manipulation 5
    norm_v1 = math.sqrt(sum(d**2 for d in v1))
    norm_v2 = math.sqrt(sum(d**2 for d in v2))
    return sum([d1*d2 for (d1,d2) in zip(v1,v2)])/(norm_v1*norm_v2)


def common_grades(other_user, target_user, scores):
    # TODO : manipulation 6
    return None


def cosine_sim_all(scores, pairs):
    cos_sim_all = []
    for (other_user, target_user) in pairs:
        (v_other, v_target) = common_grades(other_user, target_user, scores)
        cos_sim_all.append((other_user, target_user, cosine_sim(v_other, v_target)))
    return cos_sim_all


def collaborative_filtering(scores, target, n_neighbors=5, similarity_fun=None, graph=None):
    target_user, target_item = target  # une paire (utilisateur, item) pour laquelle on veut prédire la note
    
    # détermination de la fonction de similarité utilisée
    if similarity_fun is None: # si pas de fonction de similarité définie en paramètre
        if graph is not None: # si un graph a été fourni en paramètre
            similarity_fun = nx.adamic_adar_index # fonction de sim. = score Adamic-Adar
        else:
            similarity_fun = cosine_sim_all # sinon fonction de sim. = similarité cosinus

    # détermination des voisins candidats 
    if graph is not None: # si un graph a été fourni
        list_neighbors = [n for n in graph.nodes() if (n, target_item) in scores.keys()] # tous les noeuds correspondant à un utilisateur ayant noté l'item cible
    else: # sinon
        list_neighbors = [user for (user, item) in scores.keys() if item == target_item and user != target_user] # tous les utilisatuers ayant noté l'item cible

    triplets = []
    target_score = 0.
    # calcul des similarité entre l'utilisateur cible et les voisins candidats : liste de triplets (voisin, utilisateur cible, similarité)
    if len(list_neighbors):
        triplets = similarity_fun(graph if graph is not None else scores, [(n, target_user) for n in list_neighbors])

        # TODO : manipulation 3

    # ci-dessous : ajout du terme de moyenne
    # récupération des notes de l'utilisateur cible (pour calcul de la moyenne)
    target_user_scores = [v for k, v in scores.items() if k[0] == target_user]
    if len(target_user_scores) == 0: # si on n'a récupéré aucun score
        target_score += sum(scores.values()) / len(scores) # on utilise la moyenne globale des scores
    else: # sinon 
        target_score += sum(target_user_scores) / len(target_user_scores) # on utilise la moyenne des scores de l'utilisateur cible 
    return target_score


def user_based_collaborative_filtering(scores, target, n_neighbors=5, similarity_fun=None, graph=None):
    return collaborative_filtering(scores, target, n_neighbors, similarity_fun, graph)


def item_based_collaborative_filtering(scores, target, n_neighbors=5, similarity_fun=None, graph=None):
    # TODO : manipulation 8
    return None


def generic_common_neighbors(g, u, v):
    list_common_neighbors = []
    for w in g.nodes():
        if (g.has_edge(u, w) and g.has_edge(w, v)) or (g.has_edge(v, w) and g.has_edge(w, u)):
            list_common_neighbors.append(w)
    return list_common_neighbors


def generic_adamic_adar(g, ebunch=None):
    if ebunch is None:
        ebunch = nx.non_edges(g)

    def predict(u, v):
        return sum([1. / math.log(g.degree(w)) for w in generic_common_neighbors(g, u, v)])

    return [(u, v, predict(u, v)) for u, v in ebunch]