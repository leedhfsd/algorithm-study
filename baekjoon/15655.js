const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
const [N, M] = input.shift().trim().split(' ').map(Number);
const num = input.shift().trim().split(' ').map(Number);
num.sort((a, b) => a - b);
let result = '';
let arr = [];
const isUsed = Array.from({length: M}, () => 0);

const answer = (n) => {
  if (n === M) {
    result += arr.join(' ') + "\n";
    return;
  }
  let start = 0;
  if (n !== 0) start = num.indexOf(arr[n-1]) + 1;
  for (let i = start; i < N; i++) {
    if (!isUsed[i]) {
      arr.push(num[i]);
      isUsed[i] = 1;
      answer(n + 1);
      isUsed[i] = 0;
      arr.pop();
    }
  }
}

answer(0);
console.log(result);
