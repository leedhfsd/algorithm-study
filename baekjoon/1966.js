const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

const count = parseInt(input.shift());
for (let i = 1; i <= count ; i++) {
  let N, M;
  let arr = [];
  [N, M] = input[2 * (i - 1)].split(' ').map(Number);
  arr = input[2 * (i - 1) + 1].split(' ').map(Number);

  let findNumIdx = M;
  let printCount = 0;
  while (arr) {
    let maxNum = Math.max(...arr);
    if (arr[0] === maxNum && findNumIdx !== 0) {
      arr.shift();
      printCount++;
      findNumIdx--;
    } else if (arr[0] === maxNum && findNumIdx === 0) {
      console.log(++printCount);
      break;
    } else if (arr[0] !== maxNum && findNumIdx !== 0) {
      temp = arr.shift();
      arr.push(temp);
      findNumIdx--;
    } else if (arr[0] !== maxNum && findNumIdx === 0) {
      temp = arr.shift();
      arr.push(temp);
      findNumIdx = arr.length - 1;
    }
  }
}
