//BigInt는 뒤에 N이 붙기 때문에 string으로 변환한다.
const fs = require("fs");
const n = parseInt(fs.readFileSync("/dev/stdin").toString());

let dp = Array.from({length: 100}, () => BigInt(0));
dp[1] = BigInt(1);
dp[2] = BigInt(1);
for (let i = 3; i <= n; i++) {
  dp[i] = dp[i-1] + dp[i-2];
} 
console.log(String(dp[n]));
