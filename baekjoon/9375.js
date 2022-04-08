//각각의 옷 종류의 경우의 수는 옷의 수 + 입지 않는 경우의수 
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const totalCase = parseInt(input.shift());
let result = '';

for (let i = 0; i < totalCase; i++) {
  let testCase = parseInt(input.shift())
  if (testCase === 0){
    result += '0\n';
    continue;
  }
  let table = new Object();
  let arr = [];
  let sum = 1;
  for (let j = 0; j < testCase; j++) {
    let [name, kind] = input.shift().trim().split(' ');
    if (!table[kind]){
      table[kind] = [name];
    } else {
      table[kind].push(name);
    }
  }
  arr = Object.values(table).map((item) => item.length);
  for (let k = 0; k < arr.length; k++) {
    sum *= (arr[k] + 1);
  }
  result += `${sum-1}\n`;
}
console.log(result);
