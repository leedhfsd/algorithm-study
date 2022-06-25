const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

let [row, col, stkNum] = input.shift().split(' ').map(Number);
const paper = new Array(row);
for (let i = 0; i < row; i++) {
  paper[i] = new Array(col).fill(0);
}
const sticker = [];
let ans = 0;
let idx = 0;
for (let i = 0; i < stkNum; i++) {
  let [row, col] = input[idx].split(' ').map(Number);
  sticker.push(input.slice(idx+1, idx+1+row).map((v)=> v.split(' ').map(Number)));
  idx += row + 1;
}

const rotate = (arr) => { 
  let [row, col] = [arr.length, arr[0].length];
  let rotateArr = Array.from({length: col});
  for (let i = 0; i < col; i++) {
    rotateArr[i] = new Array(row).fill(0);
  }

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      rotateArr[j][row-i-1] = arr[i][j];
    }
  }
  return rotateArr;
}

const isPasted = (stk, x, y) => {
  for (let i = 0; i < stk.length; i++) {
    for (let j = 0; j < stk[0].length; j++) {
      if (x+i >= row || y+j >= col) 
        return false;
      if (paper[x+i][y+j] === 1 && stk[i][j] === 1) 
        return false;
    }
  }
  for (let i = 0; i < stk.length; i++) {
    for (let j = 0; j < stk[0].length; j++) {
      if (stk[i][j] === 1) {
        paper[x+i][y+j] = 1;
      }
    }
  }
  return true;
}

while (stkNum) {
  for (let i = 0; i < 4; i++) {
    let flag = false;
    let num = sticker.length - stkNum;
    for (let j = 0; j < row; j++) {
      if (flag) break;
      for (let k = 0; k < col; k++) {
        if (isPasted(sticker[num], j, k)) {
          flag = true;
          break;
        }
      }
    }
    if (!flag)
      sticker[num] = rotate(sticker[num]);
    else if (flag) {
      break;
    }
  }
  stkNum--;
}

for (let i = 0; i < row; i++) {
  for (let j = 0; j < col; j++) {
    if (paper[i][j] === 1) {
      ans++;
    }
  }
}
console.log(ans);
