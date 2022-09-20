def largest_component(graph):
    visited = set()
    max_c = 0
    for node in graph:
        max_c = max(max_c, explore(graph, node, visited))
    return max_c, "Final"


"""def explore_it(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    c = 1
    stack = [node]
    for neighbor in graph[node]:
        stack.append(neighbor)
        c += 1
        print(c)
    return c
"""


def explore(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    c = 1
    for neighbor in graph[node]:
        c += explore(graph, neighbor, visited)
        print(c)
    print(c, "Second Final")
    return c


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}

print(largest_component(graph))
