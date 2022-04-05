const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [n, k] = input[0].split(' ').map(Number);
let coin = input.slice(1).map(Number).sort((a, b) => b - a);
let sum = k;
let count = 0;

for (let i = 0; i < coin.length; i++) {
  if (sum < coin[i]) continue;
  else {
    let flag = true;
    while (sum > 0 && flag) {
      sum -= coin[i];
      count++;
      if (sum < 0) {
        sum += coin[i];
        count--;
        flag = false;
      }
    }
  }
}
console.log(count);
