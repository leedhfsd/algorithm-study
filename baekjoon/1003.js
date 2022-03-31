const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n').map(Number);
const testCase = input.shift();
let maxFibo = Math.max(...input);
let dp = [];
for (let i = 0 ; i <= maxFibo; i++) {
  dp.push([0,0]);
}
dp[0] = [1,0];
dp[1] = [0,1];

for (let i = 2; i <= maxFibo; i++) {
  dp[i][0] = dp[i-1][0] + dp[i-2][0];
  dp[i][1] = dp[i-1][1] + dp[i-2][1];
}

for (let i = 0; i < testCase; i++) {
  let fibo = input[i];
  console.log(dp[fibo][0], dp[fibo][1]);
}
