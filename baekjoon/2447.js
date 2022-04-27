const fs = require("fs");
const input = parseInt(fs.readFileSync("/dev/stdin").toString().trim());
const arr =  Array.from(Array(input), () => Array(input).fill(" "));

const solve = function(x, y, n) {
  
  if (n === 1) {
    arr[x][y] = "*";
    return;
  }
  let len = n / 3;
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (i === 1 && j === 1) {
        continue;
      } 
      solve(x + len * i, y + len * j, len);
    }
  }
  return;
}

solve(0,0,input);
arr.forEach((v) => {
  console.log(v.join(''));
})
