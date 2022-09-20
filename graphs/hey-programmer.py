import collections


def dfp(graph, source):
    """
    depth first print
    iterative version
    """
    stack = [source]
    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)


def dfp_rec(graph, source):
    """
    depth first print
    recursive version
    Time O(e)
    Space O(n)
    """

    print(source)
    for neighbor in graph[source]:
        dfp_rec(graph, neighbor)


# breadth first print
def bfp(graph, source):
    queue = collections.deque([source])
    while queue:
        current = queue.popleft()
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}

bfp(graph, "a")
