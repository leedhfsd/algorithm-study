// index를 늘리는 경우는 메모리 초과가 발생함
// 시간을 줄이는 법은 queue를 연결리스트로 구현해서 shift() 대신 dequeue()를 구현해서 사용
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const testCase = parseInt(input.shift());
let answer = '';

const bfs = function(a, b) {
  let queue = [];
  let visited = Array.from({length: 10000}, () => 0);
  queue.push([a, ""]);
  visited[a] = 1;
  
  while (queue.length > 0) {
    let [x, result] = queue.shift();
    if (x === b) return result;

    nx = x * 2;
    if (nx > 9999) nx = nx % 10000;
    if (visited[nx] === 0) {
      visited[nx] = 1;
      let nResult = result + "D";
      queue.push([nx, nResult]);
    }

    nx = x - 1;
    if (x === 0) nx = 9999;
    if (visited[nx] === 0) {
      visited[nx] = 1;
      let nResult = result + "S";
      queue.push([nx, nResult]);
    }

    nx = x % 1000 * 10 + Math.floor(x / 1000);
    if (visited[nx] === 0) {
      visited[nx] = 1;
      let nResult = result + "L";
      queue.push([nx, nResult]);
    }

    nx = x % 10 * 1000 + Math.floor(x / 10);
    if (visited[nx] === 0) {
      visited[nx] = 1;
      let nResult = result + "R";
      queue.push([nx, nResult]);
    }
  }
}

for (let i = 0; i < testCase; i++) {
  let [a, b] = input[i].trim().split(' ').map(Number);
  answer += `${bfs(a, b)}\n`;
}
console.log(answer);
