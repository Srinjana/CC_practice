# Given a directed graph, check whether the graph contains a cycle or not. Your function should return true if the given graph contains at least one cycle, else return false. For example, the following graph contains three cycles 0 -> 2 -> 0, 0 -> 1 -> 2 -> 0 and 3 -> 3, so your function must return true.
# Algorithm:
# Create the graph using the given number of edges and vertices.
# Create a recursive function that initializes the current index or vertex, visited, and recursion stack.
# Mark the current node as visited and also mark the index in recursion stack.
# Find all the vertices which are not visited and are adjacent to the current node. Recursively call the function for those vertices, If the recursive function returns true, return true.
# If the adjacent vertices are already marked in the recursion stack then return true.
# Create a wrapper class, that calls the recursive function for all the vertices and if any function returns true return true. Else if for all vertices the function returns false return false.

# Python program to detect cycle in a graph

from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def hasCycleUtil(self, v, visited, recStack):
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours if any neighbour is visited and in recStack then graph is cyclic
        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.hasCycleUtil(neighbor, visited, recStack) == True:
                    return True
            elif recStack[neighbor] == True:
                return True

        # The node needs to be popped from recursion stack before function ends
        recStack[v] = False
        return False

    #  Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.hasCycleUtil(node, visited, recStack) == True:
                    return True
        return False


#  Driver program to test above functions
if __name__ == '__main__': 
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    if g.isCyclic() == 1:
        print ("Graph has a cycle")
    else:
        print ("Graph has no cycle")

