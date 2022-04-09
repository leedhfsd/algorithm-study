const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n').map(Number);

const dp = Array.from({length: 101}, () => 0);
dp[1] = 1, dp[2] = 1, dp[3] = 1; dp[4] = 2, dp[5] = 2, dp[6] = 3;
for (let i = 7; i < 101; i++) {
  dp[i] = dp[i-1] + dp[i-5];
}
input.shift();
let answer = '';
for (let i = 0; i < input.length; i++) {
  answer += `${dp[input[i]]}\n`;
}
console.log(answer);
