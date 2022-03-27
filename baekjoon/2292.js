const fs = require("fs");
const input = parseInt(fs.readFileSync("/dev/stdin").toString().trim());

let num = 1;
let stage = 1;
let arr = [];
while (num <= 6000000000) {
  arr.push(num);
  num = num + 6 * stage;
  stage++;
}

for (let i = 0; i < arr.length; i++) {
  if (arr[i] >= input) {
    console.log(i + 1);
    break;
  }
}
