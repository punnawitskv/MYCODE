def dijkstra(graph, start, target):

    pq = [(0, start, [])]
    visited = set()       
    min_dist = {start: 0} 
    
    while pq:

        pq.sort(key=lambda x: x[0])
        current_dist, current_vertex, path = pq.pop(0)
        
        if current_vertex in visited:
            continue
        
        path = path + [current_vertex]
        visited.add(current_vertex)
        
        if current_vertex == target:
            return current_dist, path
        
        for neighbor, weight in graph[current_vertex].items():
            if neighbor in visited:
                continue
                
            new_cost = current_dist + weight
            old_cost = min_dist.get(neighbor, float('inf'))
            
            if new_cost < old_cost:
                min_dist[neighbor] = new_cost
                pq.append((new_cost, neighbor, path))
    
    return float('inf'), [] 

graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'D': 12},
    'C': {'A': 2, 'D': 9, 'F': 3},
    'D': {'B': 12, 'C': 9, 'E': 7, 'G': 1},
    'E': {'D': 7, 'G': 5},
    'F': {'C': 3, 'G': 4},
    'G': {'D': 1, 'E': 5, 'F': 4}
}

def find_shortest_path():
    start_target = input(" *** Dijkstra's shortest path ***\nEnter start and target vertex : ")
    start, target = start_target.split()  
    
    distance, path = dijkstra(graph, start, target)
    
    if distance < float('inf'):
        print(f"Shortest distance is {distance}")
        print(f"And the path is {path}")
    else:
        print(f"No path found from {start} to {target}")

find_shortest_path()