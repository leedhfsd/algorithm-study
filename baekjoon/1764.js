const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let [n, m] = input.shift().trim().split(' ').map(Number);
let name = input.map((item) => item.replace(/\r/g,""));
let nd = {};
let answer = [];
for (let i = 0; i < n; i++) {
  if (!nd[name[i]]) {
    nd[name[i]] = name[i];
  }
}

for (let i = n; i < name.length; i++) {
  if (nd[name[i]]) {
    answer.push(name[i]);
  } 
}
console.log(answer.length);
console.log(answer.sort().join('\n'));
