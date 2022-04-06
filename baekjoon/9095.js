const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n').map(Number);

let testCase = input[0];
let inp = input.slice(1);
let dp = Array.from({length: Math.max(...inp) + 1}, () => 0);
let answer = '';
dp[1] = 1, dp[2] = 2, dp[3] = 4;
for (let i = 4; i <= Math.max(...inp); i++) {
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
}
for (let i = 0; i < testCase; i++) {
  let num = inp[i];
  answer += `${dp[num]}\n`;
}

console.log(answer);
