const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
const [N, M] = input.shift().trim().split(' ').map(Number);
const num = input.shift().trim().split(' ').map(Number).sort((a, b) => a - b);
let result = '';
let arr = [];
const isUsed = Array.from({length: N}, () => 0);
const answer = function(k) {
  if (k === M) {
    result += arr.join(' ') + "\n";
    return;
  }

  let temp = 0;
  let start = 0;
  if (k !== 0) start = num.indexOf(arr[k-1]) + 1;
  for (let i = start; i < num.length; i++) {
    if (!isUsed[i] && temp !== num[i]) {
      isUsed[i] = 1;
      arr.push(num[i]);
      temp = arr[k];
      answer(k+1);
      isUsed[i] = 0;
      arr.pop();
    }
  }
}
answer(0);
console.log(result);
