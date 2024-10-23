def create_weighted_graph(pairs):
    graph = {}
  
    for pair in pairs:
        start, weight, end = pair
        weight = int(weight)
        if start not in graph:
            graph[start] = []
        if end not in graph:  
            graph[end] = []
        graph[start].append((end, weight))
    
    return graph


def dijkstra_no_heap(graph, start):
  
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    shortest_paths = {start: [start]}
    
    while unvisited:
     
        current_node = None
        for node in unvisited:
            if current_node is None or distances[node] < distances[current_node]:
                current_node = node
        
      
        if distances[current_node] == float('inf'):
            break
        

        unvisited.remove(current_node)
        
    
        for neighbor, weight in graph.get(current_node, []):
            distance = distances[current_node] + weight
            
      
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]
    
    return distances, shortest_paths


def print_shortest_paths(start, target, shortest_paths):
    if target in shortest_paths:
        print(f"{start} to {target} : {'->'.join(shortest_paths[target])}")
    else:
        print(f"Not have path : {start} to {target}")


graph_input, query_input = input("Enter : ").split('/')


pairs = [pair.split() for pair in graph_input.split(',')]
graph = create_weighted_graph(pairs)


queries = [query.split() for query in query_input.split(',')]


for query in queries:
    start_node, target_node = query[0], query[1]
    
 
    distances, shortest_paths = dijkstra_no_heap(graph, start_node)
    
   
    print_shortest_paths(start_node, target_node, shortest_paths)