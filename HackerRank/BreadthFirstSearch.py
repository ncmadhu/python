# Enter your code here. Read input from STDIN. Print output to STDOUT
def breadth_search(start_pos, num_nodes, edge_dict):

    visited = set()
    queue = [start_pos]
    distance_list = [-1] * num_nodes
    distance_list[start_pos - 1] = 0
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for edge in edge_dict[node]:
                if distance_list[edge - 1] == -1:                    
                    distance_list[edge - 1] = distance_list[node - 1] + 6
            queue.extend(edge_dict[node] - visited)
            
    return distance_list

t = int(raw_input().strip())
for i in range(t):
    num_nodes, num_edges = map(int, raw_input().strip().split())
    edge_dict = {}
    for e in range(num_edges):
        n1, n2 = map(int, raw_input().strip().split())
        edge_dict.setdefault(n1, set()).add(n2)
        edge_dict.setdefault(n2, set()).add(n1)
        
    for i in range(1, num_nodes + 1):
        if i not in edge_dict.keys():
            edge_dict.setdefault(i,set())
            
    start_pos = int(raw_input().strip())    
    edge_list = breadth_search(start_pos, num_nodes, edge_dict)
    solution = [str(distance) for distance in edge_list if distance != 0]
    print " ".join(solution)
        
        