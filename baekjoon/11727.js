const fs = require("fs");
const input = parseInt(fs.readFileSync("/dev/stdin").toString().trim());
const dp = Array.from({length: 1001}, () => 0);
dp[1] = 1, dp[2] = 3, dp[3] = 5;
for (let i = 4; i < dp.length; i++) {
  dp[i] = (2 * dp[i-2] + dp[i-1]) % 10007;
}
console.log(dp[input]);
