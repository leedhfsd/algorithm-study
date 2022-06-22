const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

const n = parseInt(input.shift());
const arr = input[0].split(' ').map(Number);
let max = Number.MIN_SAFE_INTEGER;
let sum = 0;

for (let i = 0; i <= n-1; i++) {
  if (sum < 0) {
    sum = arr[i];
    max = Math.max(max, sum);
  } else if (sum >= 0) {
    sum = sum + arr[i]
    max = Math.max(max, sum);
  }
}
console.log(max);
