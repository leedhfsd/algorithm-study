const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n').map(Number);

const N = parseInt(input.shift());
let dp = Array.from({length: 100001}, () => 0);
let num = Array.from({length: 100001}, () => 0);

for (let i = 2; i <= N; i++) {
  dp[i] = dp[i-1] + 1;
  num[i] = i-1;
  
   if (i % 2 === 0 && dp[i] > dp[i/2] + 1) {
    dp[i] = dp[i/2] + 1;
    num[i] = i/2;
   }
   if (i % 3 === 0 && dp[i] > dp[i/3] + 1) {
    dp[i] = dp[i/3] + 1;
    num[i] = i/3;
   }
}

let end = N;
let answer = "";

while (true) {
  answer += `${end} `;
  if (end === 1) {
    break;
  }
  end = num[end];
}
console.log(dp[N]);
console.log(answer);
