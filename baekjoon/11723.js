// 메모리 제한이 있어 자바스크립트로 통과가 불가능 한 문제.
const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
const testCase = parseInt(input.shift())
let set = new Set();
let answer = '';
for (let i = 0; i < testCase; i++) {
  let [inst, value] = input[i].trim().split(' ');
  if (inst === "add") {
    set.add(value);
  } else if (inst === "check") {
    if (set.has(value)) {
      answer += '1\n';
    } else {
      answer += '0\n';
    } 
  } else if (inst === "remove") {
    set.delete(value);
  } else if (inst === "toggle"){
    if (set.has(value)) {
      set.delete(value);
    } else {
      set.add(value);
    }
  } else if (inst === "all") {
    let newSet = Array(20).fill().map((arr, i) => {
      return i + 1;
    })
    set = new Set(newSet);
  } else if (inst === "empty") {
    set = new Set();
  }
}
console.log(answer);
