const canConstruct = (target, strings) => {
  const n = target.length;
  const list = Array(n + 1).fill(false);
  list[0] = true;

  for (let i = 0; i <= n; i++) {
    if (!list[i]) continue;
    for (let str of strings) {
      const len = str.length;
      if (i + len <= n && target.slice(i, i + len) === str) {
        list[i + len] = true;
      }
    }
  }
  return list[n]
};

console.log(canConstruct("abcdef", ["abc", "cd", "def", "abcd"]));
