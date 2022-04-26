const fs = require("fs");
const [n, r, c] = fs.readFileSync("/dev/stdin").toString().trim().split(' ').map(Number);

const answer = function(n, r, c) {
  if (n === 0) return 0;
  let half = 1 << n - 1;
  if (half > r && half > c) return answer(n-1, r, c);
  if (half > r && half <= c) return half * half + answer(n-1, r, c-half);
  if (half <= r && half > c) return half * half * 2 + answer(n-1, r - half, c);
  return half * half * 3  + answer(n-1, r - half, c - half);
}

console.log(answer(n,r,c));
