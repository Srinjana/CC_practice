# Given a directed graph, check whether the graph contains a cycle or not. Your function should return true if the given graph contains at least one cycle, else return false. For example, the following graph contains three cycles 0 -> 2 -> 0, 0 -> 1 -> 2 -> 0 and 3 -> 3, so your function must return true.
# Steps involved in detecting cycle in a directed graph using BFS.
# Step-1: Compute in -degree(number of incoming edges) for each of the vertex present in the graph and initialize the count of visited nodes as 0.
# Step-2: Pick all the vertices with in -degree as 0 and add them into a queue(Enqueue operation)
# Step-3: Remove a vertex from the queue(Dequeue operation) and then
# Increment count of visited nodes by 1.
# Decrease in -degree by 1 for all its neighboring nodes.
# If in -degree of a neighboring nodes is reduced to zero, then add it to the queue.
# Step 4: Repeat Step 3 until the queue is empty.
# Step 5: If count of visited nodes is not equal to the number of nodes in the graph has cycle, otherwise not.

import math
import sys
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    # function to add edge to the graph
    def addEdge(self, u,v):
        self.graph[u].append(v)
    
    # checks for the presence of a cycle 
def hasCycle(n, graph):
    # Create a vector to store indegrees of all
     # vertices. Initialize all indegrees as 0.
    in_degree = [0]*n

    # Traverse adjacency lists to fill indegrees of
    # vertices. This step takes O(V+E) time
    for i in range(n):
        for j in graph[i]:
            in_degree[j] += 1

    #enqueue vertices with indegree 0
    queue = []
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i)
        
    count = 0

    while(queue):

         # dequeue and add it to topological order
        nu = queue.pop(0)

        # Iterate through all its neighbouring nodes of dequeued node u and decrease their in-degree by 1
        for v in graph[nu]:
            in_degree[v] -= 1 
            
            #enqueue vertices with indegree 0
            if in_degree[v] == 0:
                queue.append(v)

        count += 1
        
    if count == n: 
        return False
    else:
        return True


# Driver program to test above functions
if __name__ == '__main__':

    # Create a graph given in the above diagram
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(3, 4)
    g.addEdge(4, 5)

    if hasCycle(g.V, g.graph):
        print("Yes, the graph has a cycle")
    else:
        print("No, the graph has no cycle")

    

