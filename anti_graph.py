import networkx as nx

N = 28

data = []
matrix = []
w_vector = []
with open('input_with_weights.csv', 'r') as file:
    m = file.readlines()
    for i in m[:-1]:
        matrix.append([int(j) for j in i.split(',')])
    w_vector = ([float(j) for j in m[-1].split(',')])
for i in range(N):
    matrix[i][i] = 0
for i in range(N):
    for j in range(i, N):
        matrix[j][i] = matrix[i][j]

# ========================2========================
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

adjency_matrix = np.eye(N)


for i in range(N):
    for j in range(N):
        if i != j:
        #print(i,j)
            adjency_matrix[j][i] = (matrix[j][i] + 1) % 2
        else:
            adjency_matrix[i][i] = 0
        


G=nx.from_numpy_array(adjency_matrix)

#===========================3=====================
def sum_of_weights(graph):
    count = 0
    for i in graph:
        count += w_vector[i]

    return count

#==============start=======================
from time import time

start = time()

complete_subgraphs = sorted(nx.find_cliques(G), key=sum_of_weights, reverse=True)

#for c in complete_subgraphs:
for i in range(5):
    g = complete_subgraphs[i]
    print(g, sum_of_weights(g))
    
end = time()

print(end-start)

