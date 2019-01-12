# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 01:26:16 2016

@author: Carlos E. Ramírez
"""
def dijkstra(graph, start, end):
    D={}#Almacenar distancias finales
    P={}#Predecesores
    
    #Fill the dicts with default values
    for node in graph.keys():#se obtienen los nodos y almacenan en D
        D[node] = -1 #-1 para como definición de infinito
        P[node] = "" #Vertices have no predecessors
    D[start] = 0 #Se asgina distancia cero al vértice de inicio
    
    unseen_nodes = graph.keys() #Lista de los nodos, los cuales son no vistos
    
    while len(unseen_nodes) > 0:#siempre que siga habiendo elementos en no vistos
        #Select the node with the lowest value in D (final distance)
        shortest = None
        node = ''
        for temp_node in unseen_nodes:
            if shortest == None:
                shortest = D[temp_node]
                node = temp_node
            elif D[temp_node] < shortest:
                shortest = D[temp_node]
                node = temp_node
        #Remove the selected node from unseen_nodes
        unseen_nodes.remove(node)
        
        #For each child (ie: connected vertex) of the currente node
        for child_node, child_value in graph[node].items():
            if D[child_node] < D[node] + child_value:
                D[child_node] = D[node] + child_value
                #To go to child node, you have to go through node
                P[child_node] = node
    #Set a clean path
    path = []
    
    #We begin from the end
    node = end
    
    #While we are not arrived at the beginning
    while not (node == start):
        if path.count(node) == 0:
            path.insert(0,node) #Insert the predecessor of the currente node
            node = P[node] #The current node becomes its predecessor
        else:
            break
    path.insert(0,start) #Finally insert the start vertex
    return path
