
"""
Created on Wed Jan 29 08:44:21 2020

@author: gourets
"""


from defGraph import Graph

# graph défini manuellement 

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

graph = Graph(g)

# Affichage des arrêts pour aider l'utilisateur
print("Arrêts : " ,graph.nodes())

# Demande des informations d'entrées à l'utilisateur
start_node = input("arret de départ ? \n")
end_node = input("arret d'arrivée ? \n")
time = input("horaire de départ ? format hh:mm \n")

# shortest, qui calcule le chemin le plus court en nombre d'arcs
def shortest(start_node, end_node):
    paths = graph.find_all_paths(start_node, end_node)
    result = paths[0]
    for chemin in paths:
        if len(chemin) <= len(result):
            result = chemin
    print("SHORTEST \n Le chemin le plus court est ", result)


#print(shortest('CAMPUS','Courier'))
#print(graph.edges())
#print(graph.vertices())

# En fonction des arrêts de départ et d'arrivée, renvoie le sens de la ligne (True or False)
def go_or_not(start_node, end_node):
    valD = valD = 0
    for noeud in graph.nodes():
        if start_node == noeud:
            valD = graph.nodes().index(start_node)
        if end_node == noeud:
            valA = graph.nodes().index(end_node)
    if valD < valA:
        return True
    else:
        return False

# Converti les horraires en unité de temps (minutes)
def convert_go(start_node):
    val1=[]
    L=[]
    if start_node in regular_path:
        for arret in regular_date_go[start_node]:
            val1 = arret.split(':')
            if val1 != ['-']:
                tot1 = int(val1[0])*60 + int(val1[1])
                L.append(tot1)
                
    elif start_node in regular_path1:
        for arret in regular_date_go1[start_node]:
            val1 = arret.split(':')
            if val1 != ['-']:
                tot1 = int(val1[0])*60 + int(val1[1])
                L.append(tot1)

            
    return L

def convert_back(start_node):
    val1=[]
    L=[]
    if start_node in regular_path:
        for arret in regular_date_back[start_node]:
            val1 = arret.split(':')
            if val1 != ['-']:
                tot1 = int(val1[0])*60 + int(val1[1])
                L.append(tot1)
                
    elif start_node in regular_path1:
        for arret in regular_date_back1[start_node]:
            val1 = arret.split(':')
            if val1 != ['-']:
                tot1 = int(val1[0])*60 + int(val1[1])
                L.append(tot1)
            
    return L

def convert(start_node, end_node):
    if go_or_not(start_node, end_node) == True:
        return convert_go(start_node)
    elif go_or_not(start_node, end_node) == False:
        return convert_back(start_node)


# Fonction qui recupère l'index du bus en fonction de l'horaire. L'index 4 correspond au 4e bus parti depuis le début de la journée
def index_departure(start_node, end_node, time):
    heure=time.split(':')[0]
    minutes=time.split(':')[1]
    toti=int(heure)*60 + int(minutes)
    L = convert(start_node, end_node)
#    print(L)
#    print(toti)
    for Harret in L:
        if int(toti)<int(Harret):
            return L.index(Harret)
        
# Fonction calculant le trajet qui prend le moins de temps de transport      
def fastest(start_node, end_node, time):
    heure=time.split(':')[0]
    minutes=time.split(':')[1]
    toti=int(heure)*60 + int(minutes)
    paths = graph.find_all_paths(start_node, end_node)
    ListeTemps = []
    tpstot = 0
    indice = index_departure(start_node, end_node, time)
    for path in paths:
        tpstot=0
        for i in range (1,len(path)):
            if go_or_not(start_node, end_node) == True:
                a = convert_go(path[i])[indice] - convert_go(path[i-1])[indice]
                if a < 0:
                    a = convert_go(path[i])[indice+1] - convert_go(path[i-1])[indice]
            else:
                a = convert_back(path[i])[indice] - convert_back(path[i-1])[indice]
                if a <0:
                     a = convert_back(path[i])[indice+1] - convert_back(path[i-1])[indice]
            tpstot = tpstot + a
        ListeTemps.append(tpstot)
    print("FASTEST \n Chemin effectué " , paths[ListeTemps.index(min(ListeTemps))])
    heureArrivée=(toti+min(ListeTemps))//60
    minuteArrivée=(toti+min(ListeTemps))%60
    print("Temps de trajet minimal " , min(ListeTemps) , " minutes")
#    print("Arrivée à " , heureArrivée,"h",minuteArrivée)

# Fonction calculant le trajet qui arrive au plus tôt
def foremost(start_node, end_vertex, time):
    heure=time.split(':')[0]
    minutes=time.split(':')[1]
    toti=int(heure)*60 + int(minutes)
    
    paths = graph.find_all_paths(start_node, end_node)

    ListeTemps = []
    tpstot = 0
    indice = index_departure(start_node, end_node, time)
    sens = go_or_not(start_node, end_node)
    for path in paths:
        tpstot=0
        for i in range (1,len(path)):
            if sens == True:
                a = convert_go(path[i])[indice] - convert_go(path[i-1])[indice]
                if a < 0:
                    a = convert_go(path[i])[indice+1] - convert_go(path[i-1])[indice]
            else:
                a = convert_back(path[i])[indice] - convert_back(path[i-1])[indice]
                if a <0:
                     a = convert_back(path[i])[indice+1] - convert_back(path[i-1])[indice]
#            print(a)
            tpstot = tpstot + a
        ListeTemps.append(tpstot)
#    print(ListeTemps)
    if sens == True:
        tempsAttente = convert_go(paths[0][0])[indice]-toti
    else:
        tempsAttente = convert_back(paths[0][0])[indice]-toti
    print("FOREMOST \n temps d'attente à l'arrêt : " ,tempsAttente , "minutes")
    print("Chemin effectué " , paths[ListeTemps.index(min(ListeTemps))])
    heureArrivée=(toti+min(ListeTemps)+tempsAttente)//60
    minuteArrivée=(toti+min(ListeTemps)+tempsAttente)%60
#    print("Temps de trajet minimal " , min(ListeTemps)+tempsAttente , " minutes")
    print("Arrivée à " , heureArrivée,"h",minuteArrivée)

shortest(start_node,end_node)
fastest(start_node,end_node, time)
foremost(start_node,end_node, time)
#graph.add_node("z")
#print(graph.nodes())
#print(convert_go('POISY_COLLEGE'))
#paths = graph.find_all_paths('Arcadium','Place_des_Romains')
#print(paths) 
#print(paths[0][-1])   
#print(go_or_not('Courier','CAMPUS'))
#print(convert('GARE','CAMPUS'))
#print(index_departure('GARE','CAMPUS','10:15'))
#fastest('GARE','CAMPUS','10:15')
