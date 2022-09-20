from typing import List, Set


def min_islands(grid: List[List[str]]):
    min_count = float("inf")
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore_size(grid, r, c, visited)
            if 0 < size < min_count:
                min_count = size
    return min_count


def explore_size(grid: List[List[str]], r: int, c: int, visited: Set[str]):
    r_bound = 0 <= r < len(grid)
    c_bound = 0 <= c < len(grid[0])

    if not (r_bound and c_bound and grid[r][c] == 'l'):
        return 0

    key = f"{r},{c}"
    if key in visited:
        return 0
    visited.add(key)

    return (
        1
        + explore_size(grid, r - 1, c, visited)
        + explore_size(grid, r, c - 1, visited)
        + explore_size(grid, r + 1, c, visited)
        + explore_size(grid, r, c + 1, visited)
    )

    return val


grid = [
    "wlwlllllllllwlllllllllll",
    "wwwwwwwwwwwwwwlllllwwllw",
    "lllwwwwlwwwwllllllllllll",
    "wwlllllllwwwwlllllllllll",
]
grid = [
    "wlwww",
    "wlwww",
    "wwwlw",
    "wwllw",
    "lwwll",
    "llwww",
]
print("Smallest island is of size", min_islands(grid))
