//////////////////////////////////////////////////////////////////
//좌표에 대해서 브루트포스 => 시간 초과
const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
const [row, col, block] = input.shift().split(' ').map(Number);

let timeResult = Number.MAX_SAFE_INTEGER;
let heightResult = Number.MIN_SAFE_INTEGER;
const arr = input.join(" ").split(" ");

for (let i = 0; i < arr.length; i++) {
  let time = 0;
  let blockCount = 0;
  let removeCount = 0;
  for (let j = 0; j < arr.length; j++) {
    if (i === j) continue;
    if (arr[j] < arr[i]) {
      blockCount += arr[i] - arr[j];
    } else if (arr[j] > arr[i]) {
      removeCount += arr[j] - arr[i];
    }
  }
  if (blockCount <= block) {
    time = blockCount + removeCount * 2;
    timeResult = Math.min(timeResult, time);
    if (time === timeResult) {
      heightResult = Math.max(heightResult, arr[i]);
    }
  }
}

console.log(timeResult, heightResult);
/////////////////////////////////////////////////////////////////
//높이에 대해서 브루트포스 => 통과
//출처 https://tesseractjh.tistory.com/99?category=470361

const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, M, B] = input[0].split(" ").map(v => +v);
input.shift();
const land = input.join(" ").split(" ");
const heightArr = new Array(257).fill(0);
land.forEach(v => heightArr[v]++);

const answer = function (B, heightArr) {
    let addition, removal;
    let [height, curTime, minTime] = [0, 0, Number.MAX_VALUE];
    for (let i=256; i >= 0; i--) {
        addition = 0;
        removal = 0;
        heightArr.forEach((v, idx) => {
            if (i < idx) removal += (idx - i)*v;
            else addition += (i - idx)*v;
        });
        if (B < addition-removal) continue;
        curTime = addition + removal*2;
        if (minTime !== Number.MAX_VALUE && minTime < curTime) break;
        if (minTime > curTime) {
            minTime = curTime;
            height = i;
        }
    }
    if (minTime === Number.MAX_VALUE) minTime = 0;
    return `${minTime} ${height}`;
};

console.log(answer(B, heightArr));
