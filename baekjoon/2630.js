const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const N = parseInt(input.shift());
const graph = input.map((v) => v.trim().split(' ').map(Number));
let arr = [0,0];
const solve = function(x, y, n) {
  let zeroFlag = true;
  let oneFlag = true; 
  for (let i = x; i < x + n; i++) {
    for (let j = y; j < y + n; j++) {
      if (graph[i][j]) {
        zeroFlag = false;
      } else {
        oneFlag = false;
      }
      if (!zeroFlag && !oneFlag) break;
    }
  }

  if (n === 1) {
    if (graph[x][y] === 0) {
      arr[0]++;
    } else {
      arr[1]++;
    }
    return;
  }
  
  if (zeroFlag) {
    arr[0] += 1;
  } else if (oneFlag) {
    arr[1] += 1;
  } else {
    solve(x, y, n / 2);
    solve(x, y + n / 2, n / 2);
    solve(x + n / 2, y, n / 2);
    solve(x + n / 2, y + n /2 , n / 2);
  }
  return;
}
solve(0,0,N);
console.log(arr.join('\n'));
