const fs = require("fs");
const [N, M] = fs.readFileSync("/dev/stdin").toString().trim().split(' ').map(Number);

let result = '';
const arr = [];

const answer = function(k) {
  if (k === M) {
    result += arr.join(' ') + "\n";
    return;
  }

  for (let i = 1; i <= N; i++) {
    arr.push(i);
    answer(k+1);
    arr.pop();
  }
}
answer(0);
console.log(result);
