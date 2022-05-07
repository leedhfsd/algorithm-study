const fs = require("fs");
const N = parseInt(fs.readFileSync("text").toString().trim());

const isUsed1 = Array.from({length: N}, () => 0);
const isUsed2 = Array.from({length: 2*N - 1}, () => 0);
const isUsed3 = Array.from({length: 2*N - 1}, () => 0);
let count = 0;


const answer = function(cur) {
  if (cur === N) {
    count++;
    return;
  }

  for (let i = 0; i < N; i++) {
    if (isUsed1[i] || isUsed2[i+cur] || isUsed3[cur-i+N-1]) continue;
    isUsed1[i] = 1;
    isUsed2[i+cur] = 1;
    isUsed3[cur-i+N-1] = 1;
    answer(cur+1);
    isUsed1[i] = 0;
    isUsed2[i+cur] = 0;
    isUsed3[cur-i+N-1] = 0;
  }
}
answer(0);
console.log(count);
