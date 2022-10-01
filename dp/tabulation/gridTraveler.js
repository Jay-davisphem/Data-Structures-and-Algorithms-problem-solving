const makeGrid = (n, m) => {
  const grid = [];
  for (let i = 0; i <= n; i++) {
    grid.push(Array(m + 1).fill(0));
  }
  return grid;
};

const gridTraveler = (n, m) => {
  const grid = makeGrid(n, m);
  grid[1][1] = 1;
  for (let i = 0; i <= n; i++) {
    for (let j = 0; j <= m; j++) {
      if (i <= n - 1) grid[i + 1][j] += grid[i][j];
      if (j <= n - 1) grid[i][j + 1] += grid[i][j];
    }
  }
  return grid[n][m];
};
console.log(gridTraveler(30, 30));
