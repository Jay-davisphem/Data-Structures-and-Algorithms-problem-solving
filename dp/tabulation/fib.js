const fib = (n) => {
  if (n < 0) return n;
  const table = Array(n + 1).fill(0);
  table[1] = 1;
  for (let i = 0; i <= n; i++) {
    console.log(table[i + 2], "i + 2");
    table[i + 1] += table[i];
    table[i + 2] += table[i];
  }
  return table[n];
};

console.log(fib(13));
