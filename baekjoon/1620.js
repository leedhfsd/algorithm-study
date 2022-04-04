const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [num, toBeAnswered] = input[0].split(' ').map(Number);
let dict = {};
let reverseDict = {};
for (let i = 1; i <= num; i++) {
  let inp = input[i].trim();
  dict[i] = inp;
  reverseDict[inp] = i;
}
let answer = '';
for (let i = num + 1; i < input.length; i++) {
  let inp = input[i].trim();
  if (!isNaN(inp)) {
    answer += `${dict[inp]}\n`;
  } else {
    answer += `${reverseDict[inp]}\n`;
  }
}
console.log(answer);
