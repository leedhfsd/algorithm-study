const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [n, m] = input.shift().split(' ').map(Number);
const arr = input.shift().split(' ').map(Number);
let dp = Array.from({length: n + 1}, () => 0);
for (let i = 1; i <= n; i++) {
  dp[i] = dp[i-1] + arr[i-1];
}
let answer = '';
for (let i = 0; i < input.length; i++) {
  const [a, b] = input[i].split(' ').map(Number);
  answer += `${dp[b]-dp[a-1]}\n`;
}
console.log(answer);
