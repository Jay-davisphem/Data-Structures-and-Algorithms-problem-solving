from typing import List, Set


def min_islands(grid: List[List[str]]):
    min_count = float("inf")
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            min_count = min(min_count, explore(grid, r, c, visited))
    return min_count


def explore(grid: List[List[str]], r: int, c: int, visited: Set[str]):
    r_bound = 0 <= r < len(grid)
    c_bound = 0 <= c < len(grid[0])

    if not (r_bound and c_bound and grid[r][c] == "w"):
        return 0

    key = f"{r},{c}"
    if key in visited:
        return 0
    visited.add(key)

    return (
        1
        + explore(grid, r - 1, c, visited)
        + explore(grid, r, c - 1, visited)
        + explore(grid, r + 1, c, visited)
        + explore(grid, r, c + 1, visited)
    )

    return val


grid = [
    "wlwlllllllllwlllllllllll",
    "wwwwwwwwwwwwwwlllllwwllw",
    "lllwwwwlwwwwllllllllllll",
    "wwlllllllwwwwlllllllllll",
]
print("Smallest island is of size", min_islands(grid))
