//구분자 여러개 사용하고 싶은 경우 split(/[원하는문자열들]/)
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();
let arr = input.split('-');
let result = [];
let sum = 0;
for (let i = 0; i < arr.length; i++) {
  if (arr[i].includes("+")) {
    let sum = arr[i].split('+').map(Number).reduce((sum, current) => sum + current, 0);
    result.push(sum);
  } else {
    result.push(parseInt(arr[i]));
  }
}
for (let i = 0; i < result.length; i++) {
  if (result.length === 1) {
    sum = result[0];
  } else {
    sum -= result[i];
  }
}
result.length === 1 ? console.log(sum) : console.log(sum + 2 * result[0]);
