const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [L, C] = input.shift().trim().split(' ').map(Number);

let char = input.shift().trim().split(' ').sort();
let isUsed = Array.from({length: L}, () => 0);
let arr = [];
let result = '';
const check = function(arr) {
  let vowel = ["a","e","i","o","u"];
  let vowelCount = 0;
  let consonantCount = 0;
  for (let i = 0; i < arr.length; i++) {
    if (vowel.includes(arr[i])) {
      vowelCount++;
    } else {
      consonantCount++;
    }
  }
  if (vowelCount >= 1 && consonantCount >= 2) {
    return true;
  } else {
    return false;
  }
}

const answer = function(k, st) {
  if (k === L) {
    if (check(arr)) {
      result += arr.join('') + "\n";
      return;
    } else {
      return;
    }
  }
  for (let i = st; i < char.length; i++) {
    if (!isUsed[i]) {
      isUsed[i] = 1;
      arr.push(char[i]);
      answer(k+1,i+1);
      isUsed[i] = 0;
      arr.pop();
    }
  }
}
answer(0, 0);
console.log(result);
