# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 08:40:54 2020

@author: gourets
"""

#from graph import *
#import data2py
#from main0 import regularOrHolyday 


nodes = (['LYCÉE_DE_POISY', 'POISY_COLLÈGE', 'Vernod', 'Meythet_Le_Rabelais', 'Chorus', 'Mandallaz', 'GARE', 'France_Barattes', 'C.E.S._Barattes', 'VIGNIÈRES', 'Ponchy', 'PARC_DES_GLAISINS', 'PISCINE-PATINOIRE', 'Arcadium', 'Parc_des_Sports', 'Place_des_Romains', 'Courier', 'Bonlieu', 'Préfecture_Pâquier', 'Impérial', 'Pommaries', 'CAMPUS'])
graph = {
        'LYCÉE_DE_POISY' : ['POISY_COLLÈGE'],
        'POISY_COLLÈGE' : ['LYCÉE_DE_POISY','Vernod'],
        'Vernod' : ['POISY_COLLÈGE', 'Meythet_Le_Rabelais'],
        'Meythet_Le_Rabelais' : ['Vernod', 'Chorus'],
        'Chorus' : ['Meythet_Le_Rabelais', 'Mandallaz'],
        'Mandallaz' : ['GARE', 'Chorus'],
        'GARE' : ['Mandallaz', 'France_Barattes', 'Bonlieu','Courier'],
        'France_Barattes' : ['C.E.S._Barattes','GARE'],
        'C.E.S._Barattes' : ['France_Barattes','VIGNIÈRES'],
        'VIGNIÈRES' : ['Ponchy','C.E.S._Barattes','CAMPUS','Pommaries'],
        'Ponchy' : ['VIGNIÈRES','PARC_DES_GLAISINS'],
        'PARC_DES_GLAISINS' : ['Ponchy','PISCINE-PATINOIRE'],
        'PISCINE-PATINOIRE' : ['PARC_DES_GLAISINS','Arcadium'],
        'Arcadium' : ['PISCINE-PATINOIRE','Parc_des_Sports'],
        'Parc_des_Sports' : ['Place_des_Romains','Arcadium'],
        'Place_des_Romains' : ['Parc_des_Sports','Courier'],
        'Courier' : ['Place_des_Romains','GARE'],
        'Bonlieu' : ['GARE','Préfecture_Pâquier'],
        'Préfecture_Pâquier' : ['Bonlieu','Impérial'],
        'Impérial' : ['Préfecture_Pâquier','Pommaries'],
        'Pommaries' : ['Impérial','VIGNIÈRES'],
        'CAMPUS' : ['VIGNIÈRES'],
        }

a = ([('LYCÉE_DE_POISY', 'POISY_COLLÈGE'),('POISY_COLLÈGE', 'Vernod'),('Vernod', 'Meythet_Le_Rabelais'),('Meythet_Le_Rabelais', 'Chorus'),('Chorus', 'Mandallaz'),('Mandallaz', 'GARE'),('GARE', 'France_Barattes'),('France_Barattes', 'C.E.S._Barattes'),('C.E.S._Barattes', 'VIGNIÈRES'),('VIGNIÈRES', 'Ponchy'),('Ponchy', 'PARC_DES_GLAISINS'),('PISCINE-PATINOIRE','Arcadium'),('Arcadium','Parc_des_Sports'),('Parc_des_Sports','Place_des_Romains'),('Place_des_Romains','Courier'),('Courier','GARE'),('GARE','Bonlieu'),('bonlieu','Préfecture_Pâquier'),('Préfecture_Pâquier','Impérial'),('Impérial','Pommaries'),('Pommaries','VIGNIÈRES'),('VIGNIÈRES', 'CAMPUS')])  

class Node:
    
    def __init__(self, valeur, neighbors=[]):
        self.valeur=valeur
        self.neighbors=neighbors
        
        
#class Graph0(Node):
#    
#    def __init__(self,labels,children=[]):
#        super().__init__(labels, children)
#        
#    def root(self):
#        return self
#    
#    def generate_edges(graph):
#        edges = []
#        for node in graph:
#            for neighbour in graph[node]:
#                edges.append((node, neighbour))
#
#        return edges
#    
#    #print(generate_edges(graph))
    
class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
#            print(self.__graph_dict[vertex])
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

#    def __str__(self):
#        res = "vertices: "
#        for k in self.__graph_dict:
#            res += str(k) + " "
#        res += "\nedges: "
#        for edge in self.__generate_edges():
#            res += str(edge) + " "
#        return res

#    def edges_weight
        
    def find_path(self, start_vertex, end_vertex, path=None):
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path: 
                    return extended_path
        return None
    
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths: 
                    paths.append(p)
        return paths

if __name__ == "__main__":
    
    g = {
        'LYCÉE_DE_POISY' : ['POISY_COLLÈGE'],
        'POISY_COLLÈGE' : ['LYCÉE_DE_POISY','Vernod'],
        'Vernod' : ['POISY_COLLÈGE', 'Meythet_Le_Rabelais'],
        'Meythet_Le_Rabelais' : ['Vernod', 'Chorus'],
        'Chorus' : ['Meythet_Le_Rabelais', 'Mandallaz'],
        'Mandallaz' : ['GARE', 'Chorus'],
        'GARE' : ['Mandallaz', 'France_Barattes', 'Bonlieu','Courier'],
        'France_Barattes' : ['C.E.S._Barattes','GARE'],
        'C.E.S._Barattes' : ['France_Barattes','VIGNIÈRES'],
        'VIGNIÈRES' : ['Ponchy','C.E.S._Barattes','CAMPUS','Pommaries'],
        'Ponchy' : ['VIGNIÈRES','PARC_DES_GLAISINS'],
        'PARC_DES_GLAISINS' : ['Ponchy','PISCINE-PATINOIRE'],
        'PISCINE-PATINOIRE' : ['PARC_DES_GLAISINS','Arcadium'],
        'Arcadium' : ['PISCINE-PATINOIRE','Parc_des_Sports'],
        'Parc_des_Sports' : ['Place_des_Romains','Arcadium'],
        'Place_des_Romains' : ['Parc_des_Sports','Courier'],
        'Courier' : ['Place_des_Romains','GARE'],
        'Bonlieu' : ['GARE','Préfecture_Pâquier'],
        'Préfecture_Pâquier' : ['Bonlieu','Impérial'],
        'Impérial' : ['Préfecture_Pâquier','Pommaries'],
        'Pommaries' : ['Impérial','VIGNIÈRES'],
        'CAMPUS' : ['VIGNIÈRES'],
        }
    
    g['LYCÉE_DE_POISY','Vernod'] = 3
    
    
    graph = Graph(g)

    print("Noeuds du graph:")
    print(graph.vertices())

    print("Arcs of graph:")
#    print(graph.edges())

    print("Ajout noeud:")
#    graph.add_vertex("z")

#    print("Vertices of graph:")
#    print(graph.vertices())
 
    print("Ajout arc:")
#    graph.add_edge({"a","z"})
    
#    print("Vertices of graph:")
#    print(graph.vertices())

#    print("Edges of graph:")
#    print(graph.edges())

    print('Ajout d un arc {"x","y"} avec de nouveaux noeuds:')
 #   graph.add_edge({"x","y"})
#    print("Vertices of graph:")
#    print(graph.vertices())
#    print("Edges of graph:")
#    print(graph.edges())



   

#stopFrom = input("arret de départ ? \n")
#stopTo = input("arret d'arrivée ? \n")
#time = input("horaire de départ ? format hh:mm \n")
#dayData = input("Jour de départ ? format dd \n")
#monthData = input("Mois de départ ? format mm en chiffre \n")

#class research:
#    
#    def __init__(self):
#        
#        self.monthData = monthData
#        self.dayData = dayData
#        self.stopFrom = stopFrom
#        self.stopTo = stopTo
#        self.time = time
        
    # dayData have to be " dd/mm "   
    
   
    
#    def userData(time, stopTo, stopFrom):
#
#       horairesDep = data2py.regular_date_go[stopTo]
#       
#g.neighbors('GARE')