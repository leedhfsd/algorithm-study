const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split('\n');

const N = parseInt(input.shift());
const cost = input.map((item) => item.split(' ').map(Number));

const dp = new Array(N);
for (let i = 0; i < N; i++) {
    dp[i] = new Array(3).fill(0);
}
dp[0] = cost[0];

for (let i = 1; i < N; i++) {
    dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + cost[i][0];
    dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + cost[i][1];
    dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + cost[i][2];
}
console.log(Math.min(...dp[N-1]));
