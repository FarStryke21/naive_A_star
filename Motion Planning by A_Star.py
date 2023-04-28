
"""
Created on Sat Nov  6 15:36:34 2021

@author: TaurusSilver_AC
"""
#imports
import csv
import math

with open('edges.csv', newline='') as f:
    reader = csv.reader(f)
    edges = list(reader)
    edges = [[float(y) for y in x] for x in edges]  #csv has String values. Convert to float.

with open('nodes.csv', newline='') as f:
    reader = csv.reader(f)
    nodes = list(reader)
    nodes = [[float(y) for y in x] for x in nodes]  #csv has String values. Convert to float.
    
#Our Inputs
start = 1
goal = 12

start_node = []
goal_node = []

#Parsing Inputs to Nodes
for node in nodes:
    if node[0] == start:
        start_node = node
    
    if node[0] == goal:
        goal_node = node


#Initialising Required lists
open_list = []
closed_list = []
past_cost = [None]*len(nodes)
parent = [None]*len(nodes)

open_list.append(start_node)

flag = False

# Function to find the neighbours
def neigbours(x):
    home = x[0]
    nbr = []
    for edge in edges:
        n1 = edge[0]
        n2 = edge[1]
        cost = edge[2]
        
        if(home == n1):
            nbr.append([n2, cost])
            continue
        
        if(home == n2):
            nbr.append([n1, cost])
            continue
    
    return nbr
        
# variable storing Infinity        
inf = math.inf

#Initialising the past cost list     
for x in range(0,len(nodes)):
    if x == 0:
        past_cost[x]=0
    else:
        past_cost[x]=inf

#Main working        
while len(open_list)>0:
    current = open_list[0]
    nbr = neigbours(open_list[0])
    nbr_nodes = []
    open_list.pop(0)
    closed_list.append(current)
    closed_list_vals = [x[0] for x in closed_list]
    for n in nbr:
        if not (n[0] in closed_list_vals):
            nbr_nodes.append(n)
    
    if current == goal_node:
        flag = True
        break
    
    for n in nbr_nodes:
        t_past_cost = past_cost[int(current[0]-1)] + n[1]
        if t_past_cost < past_cost[int(n[0]-1)]:
            past_cost[int(n[0]-1)] = t_past_cost
            open_list.append(nodes[int(n[0]-1)])
            parent[int(n[0])-1] = int(current[0])
            l = []
            for node in open_list:
                est_total_cost = past_cost[int(node[0]-1)] + node[3]
                l.append([node[0],node[1],node[2],node[3],est_total_cost])
            l = sorted(l, key=(lambda x: x[4]))
            open_list = [[x[0],x[1],x[2],x[3]] for x in l]

#Algorithm has been completed. Time for finding out if there is a path.
 
if flag:            #Success - Path Found!
    x = goal
    path = []
    path.append(x) #We will start from the goal and make our way back.
    while x is not None: #start node has no parent node, hence we stop when we reach None   
        path.append(parent[x-1])
        x = parent[x-1]
    path = path[0:len(path)-1] #The None value has been added. We trim it here.
    path.reverse() #Finally reverse the list for the actual path
    with open('path.csv', 'w') as f: #Parse list to csv 
        write = csv.writer(f)
        write.writerow(path)
        
else:               #Failure - No Path exists
    path = []
    path.append(start)  #Bot stays at starting node
    with open('path.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(path)
            
            
    

