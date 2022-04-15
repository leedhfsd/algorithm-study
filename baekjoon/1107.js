//미친 문제 다시 꼭 풀어볼 것
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const findNum = parseInt(input[0].trim());
const removed = parseInt(input[1].trim());
let removedNumArr = [];
if (removed !== 0) {
  removedNumArr =  input[2].trim().split(' ').map(Number);
}
let answer = [];
let temp = [];
let countTemp;
let count = Number.MAX_SAFE_INTEGER;
for (let i = 0; i <= 1000000; i++) {
  if (removed === 10) {
    answer = Math.abs(findNum - 100);
    break;
  }
  let flag = false;
  removedNumArr.forEach((item) => {
    if (String(i).includes(item)) {
      flag = true;
    }
  })
  if (flag) continue;
  countTemp = count;
  count = Math.min(count, Math.abs(findNum - i));
  if (count === Math.abs(findNum - i)) {
    temp = [answer[0], countTemp];
    answer = [i, count];
  }
}

let result;
if (removed === 10) {
  result = answer;
} else if (temp[0] === undefined) {
  result = Math.min(Math.abs(findNum - 100), answer[1] + String(answer[0]).length);
} else if (temp[1] !== answer[1] || temp[1] === answer[1]) {
  result = Math.min(temp[1] + String(temp[0]).length, answer[1] + String(answer[0]).length, Math.abs(findNum - 100));
}
console.log(result);
