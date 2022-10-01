/**
 * Brute force recursive
 * time: O(2^n)
 * space: O(n)
 * args: n -> integer
 * @return: fibonaci of the nth integer
 */
let fib = (n) => {
  if (n < 2) return n;
  return fib(n - 2) + fib(n - 1);
};

/**
 * iterative
 * time: O(n)
 * space: O(1)
 */
fibIt = (n) => {
  let prev = 0n,
    curr = 1n;

  let res = curr;
  for (let i = 1; i < n; i++) {
    res = prev + curr;
    prev = curr;
    curr = res;
  }
  return res;
};

/**
 * DP
 * time: O(n)
 * space: O(n)
 */
fib = (n, memo = {}) => {
  if (n in memo) return memo[n];
  if (n < 2n) return n;
  const ans = fib(n - 2n, memo) + fib(n - 1n, memo);
  memo[n] = ans;
  return ans;
};

console.log(fibIt(BigInt(3)));
console.log(fibIt(BigInt(13)));
console.log(fibIt(BigInt(30)));
console.log(fibIt(BigInt(35)));
console.log(fibIt(BigInt(500000)));

console.log();

console.log(fib(BigInt(3)) === fib(BigInt(3)));
console.log(fib(BigInt(13)) === fib(BigInt(13)));
console.log(fib(BigInt(30)) === fib(BigInt(30)));
console.log(fib(BigInt(35)) === BigInt(35));
console.log(fib(BigInt(5000)) === fib(BigInt(5000)));
