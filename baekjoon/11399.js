const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const people = parseInt(input.shift().trim());
const time = input[0].split(' ').map(Number).sort((a, b) => a - b);
let sum = 0;
let total = 0;
for (let i = 0; i < people; i++) {
  sum += time[i];
  total += sum;
}
console.log(total);
