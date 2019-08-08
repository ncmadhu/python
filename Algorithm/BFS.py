# Author: Madhu Chakravarthy
# Date: 21-04-2017

'''
1. Add edges for each node
2. Mark all nodes as not visited
3. Get the start node and add to queue
4. Loop until queue is empty
   1. Pop first node from queue
   2. Mark as visited
   3. Print the node
   4. Get edges of the node
   5. Loop edges of the node and add to queue if not visited already
'''

from collections import defaultdict

class Graph(object):

    def __init__(self):

        self.graph = defaultdict(list)


    def addEdge(self, node, edge):

        self.graph[node].append(edge)


    def BreadthFirstTraversal(self, node):

        queue = []
        visited = [False] * len(self.graph)

        queue.append(node)

        while queue:
            n = queue.pop(0)
            visited[n] =  True

            print n

            for i in self.graph[n]:
                if not visited[i]:
                    queue.append(i)


if __name__ == "__main__":

    graph = Graph()
    graph.addEdge(0,1)
    graph.addEdge(0,2)
    graph.addEdge(1,2)
    graph.addEdge(2,0)
    graph.addEdge(2,3)
    graph.addEdge(3,4)
    graph.addEdge(4,3)

    graph.BreadthFirstTraversal(2)
        
        
