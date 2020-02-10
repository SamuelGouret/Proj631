# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 08:40:54 2020

@author: gourets
"""

#from graph import *
#import data2py
#from main0 import regularOrHolyday 

data_file_name = '2_Piscine-Patinoire_Campus.txt'

try:
    with open(data_file_name, 'r') as f:
        content2 = f.read()
        
except OSError:
    # 'File not found' error message.
    print("File not found")

f.close()

data_file_name = '1_Poisy-ParcDesGlaisins.txt'

try:
    with open(data_file_name, 'r') as h:
        content1 = h.read()
        
except OSError:
    # 'File not found' error message.
    print("File not found")

h.close()

def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
    #print(splitted_dates)
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    return dic

slited_content = content2.split("\n\n")
regular_path = slited_content[0]
regular_date_go = dates2dic(slited_content[1])
regular_date_back = dates2dic(slited_content[2])
we_holidays_path = slited_content[3]
we_holidays_date_go = dates2dic(slited_content[4])
we_holidays_date_back = dates2dic(slited_content[5])

slited_content = content1.split("\n\n")
regular_path1 = slited_content[0]
regular_date_go1 = dates2dic(slited_content[1])
regular_date_back1 = dates2dic(slited_content[2])
we_holidays_path1 = slited_content[3]
we_holidays_date_go1 = dates2dic(slited_content[4])
we_holidays_date_back1 = dates2dic(slited_content[5])

all_stops = regular_path.split(" N ") + regular_path1.split(" N ")




#noeuds = (['LYCÉE_DE_POISY', 'POISY_COLLÈGE', 'Vernod', 'Meythet_Le_Rabelais', 'Chorus', 'Mandallaz', 'GARE', 'France_Barattes', 'C.E.S._Barattes', 'VIGNIÈRES', 'Ponchy', 'PARC_DES_GLAISINS', 'PISCINE-PATINOIRE', 'Arcadium', 'Parc_des_Sports', 'Place_des_Romains', 'Courier', 'Bonlieu', 'Préfecture_Pâquier', 'Impérial', 'Pommaries', 'CAMPUS'])
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

# a = ([('LYCÉE_DE_POISY', 'POISY_COLLÈGE'),('POISY_COLLÈGE', 'Vernod'),('Vernod', 'Meythet_Le_Rabelais'),('Meythet_Le_Rabelais', 'Chorus'),('Chorus', 'Mandallaz'),('Mandallaz', 'GARE'),('GARE', 'France_Barattes'),('France_Barattes', 'C.E.S._Barattes'),('C.E.S._Barattes', 'VIGNIÈRES'),('VIGNIÈRES', 'Ponchy'),('Ponchy', 'PARC_DES_GLAISINS'),('PISCINE-PATINOIRE','Arcadium'),('Arcadium','Parc_des_Sports'),('Parc_des_Sports','Place_des_Romains'),('Place_des_Romains','Courier'),('Courier','GARE'),('GARE','Bonlieu'),('bonlieu','Préfecture_Pâquier'),('Préfecture_Pâquier','Impérial'),('Impérial','Pommaries'),('Pommaries','VIGNIÈRES'),('VIGNIÈRES', 'CAMPUS')])  

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

#    graph.add_node(regular_path)
    
    def nodes(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_node(self, node):
        if node not in self.__graph_dict:
            self.__graph_dict[node] = []

    def add_edge(self, edge):
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self.__graph_dict:
            self.__graph_dict[node1].append(node2)
        else:
            self.__graph_dict[node1] = [node2]

    def __generate_edges(self):
        edges = []
        for node in self.__graph_dict:
#            print(self.__graph_dict[vertex])
            for neighbour in self.__graph_dict[node]:
                if {neighbour, node} not in edges:
                    edges.append({node, neighbour})
        return edges

        
    def find_path(self, start_node, end_node, path=None):
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_node]
        if start_node == end_node:
            return path
        if start_node not in graph:
            return None
        for node in graph[start_node]:
            if node not in path:
                extended_path = self.find_path(node, end_node, path)
                if extended_path: 
                    return extended_path
        return None
    
    def find_all_paths(self, start_node, end_node, path=[]):
        graph = self.__graph_dict 
        path = path + [start_node]
        if start_node == end_node:
            return [path]
        if start_node not in graph:
            return []
        paths = []
        for node in graph[start_node]:
            if node not in path:
                extended_paths = self.find_all_paths(node, end_node, path)
                for p in extended_paths: 
                    paths.append(p)
        return paths

if __name__ == "__main__":
    
#    g = {}
    
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
    
  #  g['LYCÉE_DE_POISY','Vernod'] = 3
    
    
     
    graph = Graph(g)

    print("Noeuds du graph:")
#    print(graph.nodes())

    print("Arcs of graph:")
#    print(graph.edges())

    print("Ajout noeud:")
#    for stop in all_stops:
#     graph.add_node(stop)

#    print("Vertices of graph:")
#    print(graph.nodes())
#    print(all_stops)
    print("Ajout arc:")
#    for i in range(1,len(all_stops)):
#     graph.add_edge({all_stops[i-1],all_stops[i]})
    #graph.add_edge({"a","z"})
    
#    print("Vertices of graph:")
#    print(graph.vertices())

#    print("Edges of graph:")
#    print(graph.edges())

#    print('Ajout d un arc {"x","y"} avec de nouveaux noeuds:')
#    graph.add_edge({"x","y"})
#    print("Vertices of graph:")
#    print(graph.vertices())
#    print("Edges of graph:")
#    print(graph.edges())

    print(g)

   

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