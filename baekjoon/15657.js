const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [N, M] = input.shift().trim().split(' ').map(Number);
const num = input.shift().trim().split(' ').map(Number);
num.sort((a, b) => a - b);
let result = '';
let arr = [];

const answer = (n) => {
  if (n === M) {
    result += arr.join(' ') + "\n";
    return;
  }
  let start = 0;
  if (n !== 0) start = num.indexOf(arr[n-1]);
  for (let i = start; i < N; i++) {
    arr.push(num[i]);
    answer(n + 1);
    arr.pop();
  }
}

answer(0);
console.log(result);
