const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

const n = parseInt(input.shift());
const arr = input.map((v) => v.trim().split(' ').map(Number));
const dp = new Array(n);
for (let i = 0; i < n; i++) {
  dp[i] = new Array(n).fill(0);
}
dp[0][0] = arr[0][0];

for (let i = 1; i < n; i++) {
  for (let j = 0; j <= n-1; j++) {
    if (!arr[i][j]) arr[i][j] = 0;
    if(j === 0) {
      dp[i][j] = dp[i-1][j] + arr[i][j];
    } else {
      dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j];
    }
  }
}
console.log(Math.max(...dp[n-1]));
