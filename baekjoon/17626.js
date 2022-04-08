const fs = require("fs");
const input = parseInt(fs.readFileSync("/dev/stdin").toString().trim());

const dp = Array.from({length: 50001}, () => 0);
dp[1] = 1;
for (let i = 2; i <= input; i++) {
  dp[i] = dp[i-1] + 1;
  for (let j = 2; j*j <= i; j++){
    dp[i] = Math.min(dp[i], dp[i - j * j] +1)
  }

}
console.log(dp[input]);
