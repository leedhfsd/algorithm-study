const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

const testData = parseInt(input.shift());
for (let i = 0; i < testData; i++) {
  let answer = ''
  let height, width, place;
  [height, width, place] = input[i].split(' ').map(Number);
  let x = place % height === 0 ? Math.floor(place / height) : Math.floor(place / height) + 1;
  let y = place % height === 0 ? height : place % height;

  if (x < 10) {
    answer += `${y}0${x}`;
  } else {
    answer += `${y}${x}`;
  }
  console.log(answer);
}
