const fs = require("fs");
const [N, M] = fs.readFileSync("/dev/stdin").toString().trim().split(' ').map(Number);

let result = '';
const arr = [];
const isUsed = Array.from({length: 9}, () => 0); 
const answer = function(k) {
  if (k === M) {
    result += arr.join(' ') + "\n";
    return;
  }
  let start = 1;
  if (k != 0) start = arr[k-1] + 1;
  for (let i = start; i <= N; i++) {
    if (!isUsed[i]) {
      arr.push(i);
      isUsed[i] = 1;
      answer(k+1);
      arr.pop();
      isUsed[i] = 0;
    }
  }
}
answer(0);
console.log(result);
