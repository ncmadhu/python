# Author: Madhu Chakravarthy
# Date: 22-04-2017

from collections import defaultdict

class Graph(object):

    def __init__(self):

        self.graph = defaultdict(list)


    def addEdge(self, node, edge):

        self.graph[node].append(edge)


    def DFS(self):

        length = len(self.graph)

        visited = []

        for i in range(length):
            if i not in visited:
                self.dfsUtil(i, visited)


    def dfsUtil(self, node, visited):

        visited.append(node)
        print node

        for i in self.graph[node]:
            if i not in visited:
                self.dfsUtil(i, visited)




if __name__ == "__main__":

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.DFS()


