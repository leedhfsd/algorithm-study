const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [N, M] = input.shift().trim().split(' ').map(Number);
let num = input.shift().trim().split(' ').map(Number).sort((a, b) => a - b);

let arr = [];
let result = '';
let isUsed = Array.from({length: N}, () => 0);

const answer = function(k) {
  if (k === M) {
    result += arr.join(' ') + "\n";
    return;
  }
  let temp = 0;
  for (let i = 0; i < N; i++) {
    if (!isUsed[i] && temp !== num[i]) {
      isUsed[i] = 1;
      arr.push(num[i]);
      temp = num[i];
      answer(k+1);
      isUsed[i] = 0;
      arr.pop();
    }
  }
}
answer(0);
console.log(result);
