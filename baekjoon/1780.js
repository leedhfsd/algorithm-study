const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
const N = parseInt(input.shift());
const paper = input.map((v) => v.trim().split(' ').map(Number));
let arr = [0,0,0];

const check = function(x, y, n) {
  for (let i = x; i < x + n; i++) {
    for (let j = y; j < y + n; j++) {
      if (paper[x][y] !== paper[i][j]) return false;
    }
  }
  return true;
}

const answer = function(x, y, n) {
  if (check(x, y, n)) {
    arr[paper[x][y] + 1]++;
    return;
  }
  let len = n / 3;
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      answer(x + len * i, y + len * j, len);
    }
  }
}

answer(0, 0, N);
console.log(arr.join('\n'));
