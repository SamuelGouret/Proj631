
"""
Created on Wed Jan 29 08:44:21 2020

@author: gourets
"""


from defGraph import Graph

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

g = {
    'LYCEE_DE_POISY' : ['POISY_COLLEGE'],
    'POISY_COLLEGE' : ['LYCÉE_DE_POISY','Vernod'],
    'Vernod' : ['POISY_COLLEGE', 'Meythet_Le_Rabelais'],
    'Meythet_Le_Rabelais' : ['Vernod', 'Chorus'],
    'Chorus' : ['Meythet_Le_Rabelais', 'Mandallaz'],
    'Mandallaz' : ['GARE', 'Chorus'],
    'GARE' : ['Mandallaz', 'France_Barattes', 'Bonlieu','Courier'],
    'France_Barattes' : ['C.E.S._Barattes','GARE'],
    'C.E.S._Barattes' : ['France_Barattes','VIGNIERES'],
    'VIGNIERES' : ['Ponchy','C.E.S._Barattes','CAMPUS','Pommaries'],
    'Ponchy' : ['VIGNIERES','PARC_DES_GLAISINS'],
    'PARC_DES_GLAISINS' : ['Ponchy'],
    'PISCINE-PATINOIRE' : ['Arcadium'],
    'Arcadium' : ['PISCINE-PATINOIRE','Parc_des_Sports'],
    'Parc_des_Sports' : ['Place_des_Romains','Arcadium'],
    'Place_des_Romains' : ['Parc_des_Sports','Courier'],
    'Courier' : ['Place_des_Romains','GARE'],
    'Bonlieu' : ['GARE','Préfecture_Pâquier'],
    'Préfecture_Pâquier' : ['Bonlieu','Impérial'],
    'Impérial' : ['Préfecture_Pâquier','Pommaries'],
    'Pommaries' : ['Impérial','VIGNIERES'],
    'CAMPUS' : ['VIGNIERES'],
    }

graph = Graph(g)
print("Arrêts : " ,graph.vertices())

start_vertex = input("arret de départ ? \n")
end_vertex = input("arret d'arrivée ? \n")
time = input("horaire de départ ? format hh:mm \n")

def shortest(start_vertex, end_vertex):
    paths = graph.find_all_paths(start_vertex, end_vertex)
    result = paths[0]
    for chemin in paths:
        if len(chemin) <= len(result):
            result = chemin
    print("SHORTEST \n Le chemin le plus court est ", result)


#print(shortest('CAMPUS','Courier'))
#print(graph.edges())
#print(graph.vertices())

def go_or_not(start_vertex, end_vertex):
    valD = valD = 0
    for noeud in graph.vertices():
        if start_vertex == noeud:
            valD = graph.vertices().index(start_vertex)
        if end_vertex == noeud:
            valA = graph.vertices().index(end_vertex)
    if valD < valA:
        return True
    else:
        return False

def convert_go(start_vertex):
    val1=[]
    L=[]
    if start_vertex in regular_path:
        for arret in regular_date_go[start_vertex]:
            val1 = arret.split(':')
            if val1 != ['-']:
                tot1 = int(val1[0])*60 + int(val1[1])
                L.append(tot1)
                
    elif start_vertex in regular_path1:
        for arret in regular_date_go1[start_vertex]:
            val1 = arret.split(':')
            if val1 != ['-']:
                tot1 = int(val1[0])*60 + int(val1[1])
                L.append(tot1)

            
    return L

def convert_back(start_vertex):
    val1=[]
    L=[]
    if start_vertex in regular_path:
        for arret in regular_date_back[start_vertex]:
            val1 = arret.split(':')
            if val1 != ['-']:
                tot1 = int(val1[0])*60 + int(val1[1])
                L.append(tot1)
                
    elif start_vertex in regular_path1:
        for arret in regular_date_back1[start_vertex]:
            val1 = arret.split(':')
            if val1 != ['-']:
                tot1 = int(val1[0])*60 + int(val1[1])
                L.append(tot1)
            
    return L

def convert(start_vertex, end_vertex):
    if go_or_not(start_vertex, end_vertex) == True:
        return convert_go(start_vertex)
    elif go_or_not(start_vertex, end_vertex) == False:
        return convert_back(start_vertex)

def index_departure(start_vertex, end_vertex, time):
    heure=time.split(':')[0]
    minutes=time.split(':')[1]
    toti=int(heure)*60 + int(minutes)
    L = convert(start_vertex, end_vertex)
#    print(L)
#    print(toti)
    for Harret in L:
        if int(toti)<int(Harret):
            return L.index(Harret)
        
def fastest(start_vertex, end_vertex, time):
    heure=time.split(':')[0]
    minutes=time.split(':')[1]
    toti=int(heure)*60 + int(minutes)
#    print(toti)
    paths = graph.find_all_paths(start_vertex, end_vertex)
#    print(paths)
    ListeTemps = []
    tpstot = 0
    indice = index_departure(start_vertex, end_vertex, time)
#    indice = 2
    for path in paths:
        tpstot=0
        for i in range (1,len(path)):
            if go_or_not(start_vertex, end_vertex) == True:
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
    print("FASTEST \n Chemin effectué " , paths[ListeTemps.index(min(ListeTemps))])
    heureArrivée=(toti+min(ListeTemps))//60
    minuteArrivée=(toti+min(ListeTemps))%60
    print("Temps de trajet minimal " , min(ListeTemps) , " minutes")
    print("Arrivée à " , heureArrivée,"h",minuteArrivée)

def foremost(start_vertex, end_vertex, time):
    heure=time.split(':')[0]
    minutes=time.split(':')[1]
    toti=int(heure)*60 + int(minutes)
    
#    print(toti)
    paths = graph.find_all_paths(start_vertex, end_vertex)
#    print(paths)
    ListeTemps = []
    tpstot = 0
    indice = index_departure(start_vertex, end_vertex, time)
    sens = go_or_not(start_vertex, end_vertex)
#    indice = 2
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
    print("Temps de trajet minimal " , min(ListeTemps)+tempsAttente , " minutes")
    print("Arrivée à " , heureArrivée,"h",minuteArrivée)

shortest(start_vertex,end_vertex)
fastest(start_vertex,end_vertex, time)
foremost(start_vertex,end_vertex, time)
#print(convert_go('POISY_COLLEGE'))
#paths = graph.find_all_paths('Arcadium','Place_des_Romains')
#print(paths) 
#print(paths[0][-1])   
#print(go_or_not('Courier','CAMPUS'))
#print(convert('GARE','CAMPUS'))
#print(index_departure('GARE','CAMPUS','10:15'))
#fastest('GARE','CAMPUS','10:15')
