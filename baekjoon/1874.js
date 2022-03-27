const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n').map(Number);

const n = input.shift();
let top = 1;
const stack = [];
let inputString = '';
let resultString ='';
let answer = '';
for (let i = 0; i < input.length; i++) {
  inputString += `${input[i]}`;
  if (top <= input[i]) {
    while (top <= input[i]) {
      answer += '+\n';
      stack.push(top);
      top++;
    }
    resultString += `${stack.pop()}`;
    answer += '-\n';
  } else if (top >= input[i]) {
    resultString += `${stack.pop()}`;
    answer += '-\n';
  }
}
inputString === resultString ? console.log(answer) : console.log("NO");
