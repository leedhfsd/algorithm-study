const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const testCase = parseInt(input.shift());

let dx = [-1,-2,-2,-1,1,2,2,1];
let dy = [-2,-1,1,2,2,1,-1,-2];

for (let i = 0; i < testCase * 3; i = i + 3) {
  let len = parseInt(input[i]);
  let [x, y] = input[i+1].trim().split(' ').map(Number);
  let [nx, ny] = input[i+2].trim().split(' ').map(Number);
  let visited = Array.from(Array(len), () => Array(len).fill(0));
  let queue = [];
  let count = 0;
  queue.push([x, y]);
  while (queue.length > 0) {
    let [a, b] = queue.shift();
    if (a === nx && b === ny) break;
    for (let i = 0; i < 8; i++) {
      na = a + dx[i];
      nb = b + dy[i];

      if (0 > na || na >= len || 0 > nb || nb >= len) continue;
      if (visited[na][nb] === 0) {
        queue.push([na, nb]);
        visited[na][nb] = visited[a][b] + 1;
      }
    
    }
  }
  console.log(visited[nx][ny]);
}
