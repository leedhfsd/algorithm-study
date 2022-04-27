const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
const N = parseInt(input.shift());
const graph = input.map((v) => v.trim().split('').map(Number));

let answer = '';
const solve = function(x, y ,len) {
  if (len === 1) {
    answer += `${graph[x][y]}`;
    return;
  }
  let zeroFlag = true;
  let oneFlag = true;
  for (let i = x; i < x + len; i++) {
    for (let j = y; j < y + len; j++) {
      if (graph[i][j]) {
        zeroFlag = false;
      } else {
        oneFlag = false;
      }
    }
  }
  if (zeroFlag) {
    answer += '0';
  } else if (oneFlag) {
    answer += '1';
  } else {
    answer += '(';
    solve(x, y, len / 2);
    solve(x, y + len / 2, len / 2);
    solve(x + len / 2, y, len /2);
    solve(x + len / 2, y + len / 2, len / 2);
    answer += ')';
  }
  return;
}

solve(0,0,N);
console.log(answer);
