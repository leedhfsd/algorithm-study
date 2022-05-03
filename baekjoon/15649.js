const fs = require("fs");
const [N, M] = fs.readFileSync("/dev/stdin").toString().trim().split(' ').map(Number);

const isUsed  = Array.from({length: 9}, () => 0);
const arr = [];
let result = '';
const answer = function(n) {
  if (n === M) {
    result += arr.join(' ') + '\n';
    return;
  }

  for (let i = 1; i <= N; i++) {
    if (!isUsed[i]) {
      isUsed[i] = 1;
      arr.push(i);
      answer(n+1);
      isUsed[i] = 0;
      arr.pop();
    }
  }
}
answer(0);
console.log(result);
