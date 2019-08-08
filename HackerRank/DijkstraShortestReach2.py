# Enter your code here. Read input from STDIN. Print output to STDOUT
import heapq
def breadth_search(start_pos, num_nodes, edge_dict, edge_values):

    visited = set()
    heap_queue = []
    distance_list = [-1] * num_nodes
    distance_list[start_pos - 1] = 0
    heapq.heappush(heap_queue, (distance_list[start_pos - 1], start_pos))
    
    while len(heap_queue) != 0:
        distance, node = heapq.heappop(heap_queue)
        if node not in visited:
            visited.add(node)
            if distance_list[node - 1] == -1:
                distance_list[node - 1] == distance
            for edge in edge_dict[node]:
                if distance_list[edge - 1] == -1 or distance_list[edge - 1] > distance + min(edge_values[str(node) + "," + str(edge)]):
                    distance_list[edge - 1] = distance + min(edge_values[str(node) + "," + str(edge)])
                    heapq.heappush(heap_queue, (distance_list[edge - 1], edge))
            
    return distance_list

t = int(raw_input().strip())
for i in range(t):
    num_nodes, num_edges = map(int, raw_input().strip().split())
    edge_dict = {}
    edge_values = {}
    for e in range(num_edges):
        n1, n2, value = map(int, raw_input().strip().split())
        edge_dict.setdefault(n1, set()).add(n2)
        edge_dict.setdefault(n2, set()).add(n1)
        edge_values.setdefault(str(n1) + "," + str(n2), set()).add(value)
        edge_values.setdefault(str(n2) + "," + str(n1), set()).add(value)
    #print edge_values
        
    for i in range(1, num_nodes + 1):
        if i not in edge_dict.keys():
            edge_dict.setdefault(i,set())
            
    start_pos = int(raw_input().strip())    
    edge_list = breadth_search(start_pos, num_nodes, edge_dict, edge_values)
    solution = [str(distance) for distance in edge_list if distance != 0]
    print " ".join(solution)
        
        