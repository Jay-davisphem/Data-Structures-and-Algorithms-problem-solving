def connected_component(graph):
    visited = set()
    c = 0
    for node in graph:
        c += explore(graph, node, visited)
    return c


def explore(graph, node, visited):
    if node in visited:
        return False
    visited.add(node)

    for neighbor in graph[node]:
        explore(graph, neighbor, visited)
    return True


graph = {
    1: [2],
    2: [],
    3: [],
    4: [6],
    5: [6],
    6: [5, 8, 4, 7],
    7: [6],
    8: [6],
}

print(connected_component(graph))
