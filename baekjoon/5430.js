const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const testCase = parseInt(input.shift());
let answer = '';

for (let i = 0; i < testCase; i++) {
  let flag = true;
  let errorFlag = true;
  let func =  input.shift().trim().split('');
  let arrLength = parseInt(input.shift());
  let arr = input.shift().trim();
  if (arrLength === 0 && func.includes("D")) {
    answer += "error\n";
    continue;
  } 
  arr = arr.slice(1,arr.length-1).split(',');
  for (let j = 0; j < func.length; j++) {
    if (func[j] === "R") {
      flag = !flag;
    } else if (func[j] === "D" && arr.length === 0) {
      errorFlag = false;
      break;
    } else if (func[j] === "D" && flag) {
      arr.shift();
    } else if (func[j] === "D" && !flag) {
      arr.pop();
    } 
  }
  if (!flag && errorFlag) {
    answer += `[${arr.reverse()}]\n`;
  } else if (flag && errorFlag) {
    answer += `[${arr}]\n`;
  } else if (!errorFlag) {
    answer += 'error\n';
  }
}
console.log(answer);
