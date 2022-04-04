const fs = require("fs");
const input = parseInt(fs.readFileSync("/dev/stdin").toString().trim());

let dp = Array.from({length: 1000001}, () => 0);
for (let i = 2; i <= input; i++) {
  if (dp[input] !== 0) break;
  dp[i] = dp[i-1] + 1;
  if (i % 2 === 0) {
    dp[i] = Math.min(dp[i/2] + 1, dp[i]);
  } 
  if (i % 3 === 0) {
    dp[i] = Math.min(dp[i/3] + 1, dp[i]);
  }
}
console.log(dp[input]);
