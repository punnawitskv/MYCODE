class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def build_linked_lists(connections):
    nodes = {}
    for connection in connections.split(','):
        start, end = map(int, connection.split('>'))
        if start not in nodes:
            nodes[start] = Node(start)
        if end not in nodes:
            nodes[end] = Node(end)
        nodes[start].next = nodes[end]
    return nodes

def find_intersections(nodes):
    visited = {}
    intersections = []
    for node in nodes.values():
        current = node
        while current:
            if current in visited:
                intersections.append(current)
                break
            visited[current] = True
            current = current.next
    return intersections

def list_length_and_remove_intersection(node):
    visited = set()
    length = 0
    while node and node not in visited:
        visited.add(node)
        node = node.next
        length += 1
    return length

def merge_and_sort_remaining(nodes, intersections):
    for intersect in intersections:
        for node in nodes.values():
            if node.next == intersect:
                node.next = None
    remaining_lists = [node for node in nodes.values() if node.next or node not in [i.value for i in intersections]]
    remaining_lists = sorted(remaining_lists, key=lambda x: x.value)
    
    merged_list = []
    while any(remaining_lists):
        for i in range(len(remaining_lists)):
            if remaining_lists[i]:
                merged_list.append(remaining_lists[i].value)
                remaining_lists[i] = remaining_lists[i].next
    
    return merged_list

def main():
    input_str = input("Enter edges: ").strip()
    nodes = build_linked_lists(input_str)
    
    intersections = find_intersections(nodes)
    if intersections:
        for intersection in intersections:
            length = list_length_and_remove_intersection(intersection)
            print(f"Node({intersection.value}, size={length})")
        
        merged_list = merge_and_sort_remaining(nodes, intersections)
        print("Delete intersection then swap merge:")
        print(" -> ".join(map(str, merged_list)))
    else:
        print("No intersection")

# Run the main function to execute the program
main()
