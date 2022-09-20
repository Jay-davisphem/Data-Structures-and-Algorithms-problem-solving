from collections import defaultdict


def undirected_path(edges, node_a, node_b):
    graph = edges_to_graph(edges)
    visited = set()
    stack = [node_a]
    while stack:
        current = stack.pop()
        if current in visited:
            return False
        visited.add(current)
        if current == node_b:
            return True
        for i in graph[current]:
            if i == node_b:
                return True
            stack.append(i)
    return False


def edges_to_graph(edges):
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    return graph


edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
]
print(undirected_path(edges, "j", "m"))
