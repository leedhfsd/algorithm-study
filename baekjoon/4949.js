const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

for (let i = 0; i < input.length - 1; i++) {
  let string = input[i].split('');
  let stack = [];
  let flag = true;
  for (let j = 0; j < string.length; j++) {
    if (string[j] === "[" || string[j] === "(") {
      stack.push(string[j]);
    } else if (string[j] === "]") {
      if (stack[stack.length - 1] === "[") {
        stack.pop();
      } else {
        flag = false;
        break;
      }
    } else if (string[j] === ")") {
      if (stack[stack.length - 1] === "(") {
        stack.pop();
      } else {
        flag = false;
        break;
      }     
    }
  }
  if (flag && stack.length === 0) console.log("yes");
  else console.log("no");

}
