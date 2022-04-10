const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const testCase = parseInt(input.shift());
let arr = [];

for (let i = 0; i < testCase; i++) {
  let [a, b] = input[i].trim().split(' ').map(Number);
  arr.push([a, b, b - a]);
}
arr.sort((a, b) => {
  if (a[1] !== b[1]) {
    return a[1] - b[1];
  } else {
    return a[0] - b[0];
  }
});
let time = arr[0][1];
let count = 1;
for (let i = 0; i < testCase; i++) {
  if (i === 0) continue;
  if (arr[i][0] < time) continue;
  else {
    time = arr[i][1];
    count++;
  }
}
console.log(count);
