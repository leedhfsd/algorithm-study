const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

let result = '';
const answer = function(num, arr, isUsed, k) {
  if (k === 6) {
    result += arr.join(' ') + "\n";
    return;
  }
  let start = 0;
  if (k !== 0) start = num.indexOf(arr[k-1]);
  for (let i = start; i < num.length; i++) {
    if (!isUsed[i]) {
      isUsed[i] = 1;
      arr.push(num[i]);
      answer(num, arr, isUsed, k+1);
      isUsed[i] = 0;
      arr.pop();
    }
  }
}

for (let i = 0; i < input.length - 1; i++) {
  let num = input[i].trim().split(' ').map(Number);
  let k = num.shift();
  let isUsed = Array.from({length: k}, () => 0);
  let arr = [];
  answer(num, arr, isUsed, 0);
  result += "\n";
}

console.log(result);
