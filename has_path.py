import collections
from typing import Dict, List, Set


def has_path(
    graph: Dict[str, List[str]], src: str, dst: str, visited: Set[str] = set()
) -> bool:
    if src in visited:  # preventing cycle
        return False
    visited.add(src)
    if src == dst:
        return True
    stack = [src]
    while stack:
        current = stack.pop()
        if current == dst:
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)
    return False


def has_path_bfs(
    graph: Dict[str, List[str]], src: str, dst: str, visited: Set[str] = set()
) -> bool:
    if src in visited:  # preventing cycle
        return False
    visited.add(src)
    if src == dst:
        return True
    queue = collections.deque([src])
    while queue:
        cur = queue.popleft()
        if cur == dst:
            return True
        for neighbor in graph[cur]:
            queue.append(neighbor)
    return False


graph = {
    "f": ["g", "i"],
    "g": ["i"],
    "h": [],
    "i": ["g", "f"],
    "j": ["i"],
    "k": [],
}

print(has_path_bfs(graph, "f", "i"))
