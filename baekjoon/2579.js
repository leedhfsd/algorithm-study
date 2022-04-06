const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n').map(Number);
const stairs = input[0];
let dp = Array.from({length: 301}, () => [0,0,0]);
dp[1][1] = input[1];
dp[2][1] = input[2];
dp[2][2] = input[1] + input[2];


for (let i = 3; i <= stairs; i++) {
  dp[i][1] = Math.max(dp[i-2][1], dp[i-2][2]) + input[i];
  dp[i][2] = dp[i-1][1] + input[i];
}
console.log(Math.max(...dp[stairs]));
