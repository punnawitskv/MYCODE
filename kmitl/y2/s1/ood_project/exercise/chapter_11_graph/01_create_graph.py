def create_adj_matrix(pairs, nodes):
   
    n = len(nodes)
    adj_matrix = [[0] * n for _ in range(n)]
    
    node_index = {node: i for i, node in enumerate(nodes)}
   
    for pair in pairs:
        start, end = pair
        adj_matrix[node_index[start]][node_index[end]] = 1

    return adj_matrix

def print_adj_matrix(adj_matrix, nodes):
 
    print("   ", "  ".join(nodes))
    for i, row in enumerate(adj_matrix):
        print(f"{nodes[i]} :", ", ".join(map(str, row)))


input_pairs = input("Enter : ").split(',')
pairs = [tuple(pair.split()) for pair in input_pairs]

nodes = sorted(set([node for pair in pairs for node in pair]))


adj_matrix = create_adj_matrix(pairs, nodes)

print_adj_matrix(adj_matrix, nodes)