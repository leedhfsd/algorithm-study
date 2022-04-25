const fs = require("fs");
const input = parseInt(fs.readFileSync("text").toString().trim());
let answer = '';
const hanoi = function(start, end, level) {
  if (level === 1) {
    answer += `${start} ${end}\n`
    return;
  };
  hanoi(start, 6-start-end, level - 1);
  answer += `${start} ${end}\n`;
  hanoi(6-start-end, end, level - 1);
}
console.log(Math.pow(2,input)-1);
hanoi(1,3,input);
console.log(answer);
