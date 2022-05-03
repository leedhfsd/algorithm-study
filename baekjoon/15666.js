const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [N, M] = input.shift().trim().split(' ').map(Number);
const num = input.shift().trim().split(' ').map(Number).sort((a, b) => a - b);
let result = '';
let arr = [];

const answer = function(k, idx) {
  if (k === M) {
    result += arr.join(' ') + "\n";
    return;
  }
  let temp = 0;
  for (let i = idx; i < N; i++) {
    if (temp !== num[i]){
      arr.push(num[i]);
      temp = num[i];
      answer(k+1, i);
      arr.pop();
    }
  }
}
answer(0,0);
console.log(result);
