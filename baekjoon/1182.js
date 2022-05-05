const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [n, s] = input.shift().trim().split(' ').map(Number);
const num = input.shift().trim().split(' ').map(Number);
let count = 0;
let arr = [];
let level = 0;

const answer = function(k, idx) {
  if (k === level + 1) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
      sum += arr[i];
    }
    if (sum === s) count++
    return;
  }
  for (let i = idx; i < n; i++) {
    arr.push(num[i]);
    answer(k+1, i+1);
    arr.pop();
  }
}
while(level < n) {
  answer(0, 0);
  level++;
}
console.log(count);
