const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const wheel = [[]];
let count = parseInt(input[4]);
let spin = [];
for (let i = 0; i < 4; i++) {
  wheel.push(input[i].trim().split('').map(Number));
}
for (let i = 5; i < input.length; i++) {
  let [num, dir] = input[i].split(' ').map(Number);
  spin.push([num, dir]);
}
const clockRotate = (arr) => {
  let num = [arr.pop()];
  arr = num.concat(arr);
  return arr;
}

const counterClockRotate = (arr) => {
  let num = [arr.shift()];
  arr = arr.concat(num);
  return arr;
}

const left = (num, bool, dir) => {
  let is;
  if (!bool || num < 1 || num > 4) return;
  if (num > 1) {
    is = (wheel[num][6] !== wheel[num-1][2]);
  } 

  if (dir === 1) {
    wheel[num] = clockRotate(wheel[num]);
  } else if (dir === -1) {
    wheel[num] = counterClockRotate(wheel[num]);
  }
  left(num-1, is, dir*-1);
}

const right = (num, bool, dir) => {
  let is;
  if (!bool || num < 1 || num > 4) return;
  if (num < 4) {
    is = (wheel[num][2] !== wheel[num+1][6]);
  }
  if (dir === 1) {
    wheel[num] = clockRotate(wheel[num]);
  } else if (dir === -1) {
    wheel[num] = counterClockRotate(wheel[num]);
  }
  right(num+1, is, dir*-1);
}

for (let i = 0; i < spin.length; i++) {
  let [num , dir] = spin[i];
  left(num, true, dir);
  if (dir === 1) wheel[num] = counterClockRotate(wheel[num]); 
  else wheel[num] = clockRotate(wheel[num]);
  right(num, true, dir);

}
let ans = 0;
if (wheel[1][0] === 1) ans += 1;
if (wheel[2][0] === 1) ans += 2;
if (wheel[3][0] === 1) ans += 4;
if (wheel[4][0] === 1) ans += 8;

console.log(ans);
