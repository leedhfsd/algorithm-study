const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

let horseCount = parseInt(input.shift());
const [col, row] = input.shift().trim().split(' ').map(Number);
const graph = input.map((v) => v.trim().split(' ').map(Number));
let visited = [];
for (let i = 0; i <= horseCount; i++) {
  visited.push(Array.from(Array(row), () => Array(col).fill(0)));
}
let dx = [-1,1,0,0];
let dy = [0,0,-1,1];
let hx = [-1,-2,-2,-1,1,2,2,1];
let hy = [-2,-1,1,2,2,1,-1,-2];
let queue = [[0,0,0]];
visited[0][0][0] = 1;
let answer = -1;
while (queue.length > 0) {
  let [level, x, y] = queue.shift();
  if (x === row - 1 && y === col - 1) {
    answer = visited[level][x][y] - 1;
    break;
  }
  if (level < horseCount) {
    for (let i = 0; i < 8; i++) {
      let nx = x + hx[i];
      let ny = y + hy[i];

      if (nx < 0 || nx >= row || ny < 0 || ny >= col) continue;
      if (graph[nx][ny] === 1) continue;
      if (visited[level+1][nx][ny]) continue;
      visited[level+1][nx][ny] = visited[level][x][y] + 1;
      queue.push([level+1, nx, ny]);
    }
  }
  for (let i = 0; i < 4; i++) {
    let nx = x + dx[i];
    let ny = y + dy[i];

    if (nx < 0 || nx >= row || ny < 0 || ny >= col) continue;
    if (graph[nx][ny] === 1) continue;
    if (visited[level][nx][ny]) continue;
    visited[level][nx][ny] = visited[level][x][y] + 1;
    queue.push([level, nx, ny]);
  }

}

console.log(answer);
