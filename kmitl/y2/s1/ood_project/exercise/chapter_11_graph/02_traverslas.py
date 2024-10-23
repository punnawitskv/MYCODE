class Graph:
    def __init__(self):
        self.graph = {}  
    

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)


    def dfs(self):
        visited = set()  
        result = []

        def dfs_recursive(v):
            visited.add(v)
            result.append(v)

            for neighbor in sorted(self.graph[v]):
                if neighbor not in visited:
                    dfs_recursive(neighbor)


        for vertex in sorted(self.graph.keys()):
            if vertex not in visited:
                dfs_recursive(vertex)
        
        return result


    def bfs(self):
        visited = set()
        result = []

        def bfs_from_vertex(start):
            queue = [start]
            visited.add(start)
            
            while queue:
                v = queue.pop(0)
                result.append(v)

                for neighbor in sorted(self.graph[v]):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)


        for vertex in sorted(self.graph.keys()):
            if vertex not in visited:
                bfs_from_vertex(vertex)
        
        return result


def build_graph(input_data):
    edges = input_data.split(',')
    

    for edge in edges:
        if len(edge.split()) != 2:
            print("Error: Input format should be like 'A B, B C, A D'. Please check your input.")
            return
    
    g = Graph()
    
    for edge in edges:
        u, v = edge.split()
        g.add_edge(u, v)
    

    dfs_result = g.dfs()
    bfs_result = g.bfs()
    

    print("Depth First Traversals :", ' '.join(dfs_result))
    print("Bredth First Traversals :", ' '.join(bfs_result))


input_data = input("Enter : ")
build_graph(input_data)
