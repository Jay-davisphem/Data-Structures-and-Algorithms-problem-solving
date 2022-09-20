from typing import List, Set


def islands_count(grid: List[List[str]]):
    count = 0
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            count += explore(grid, r, c, visited)
    return count


def explore(grid: List[List[str]], r: int, c: int, visited: Set[str]):
    r_bound = 0 <= r < len(grid)
    c_bound = 0 <= c < len(grid[0])

    if not (r_bound and c_bound and grid[r][c] == "w"):
        return False

    key = f"{r},{c}"
    if key in visited:
        return False
    visited.add(key)

    explore(grid, r - 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c + 1, visited)
    return True


grid = [
    "wlwlllllllllw",
    "wwwlllllwwllw",
    "lllwwwwlwwwwl",
    "wwlllllllwwww",
]

print("Islands count is", islands_count(grid))
