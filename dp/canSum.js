let canSum = (target, list, memo = {}) => {
  //if (target in memo) return memo[target];
  if (target === 0) return true;
  if (target < 0) return false;

  for (let val of list) {
    const rem = target - val;
    if (canSum(rem, list, memo)) {
      //memo[target] = true;
      return true;
    }
  }
  //memo[target] = false;
  return false;
};

console.log(canSum(300, [7, 14]));
