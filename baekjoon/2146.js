const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const len = parseInt(input.shift());
const graph = input.map((v) => v.trim().split(' ').map(Number));
let bridge = Number.MAX_SAFE_INTEGER;
let visited = Array.from(Array(len), () => Array(len).fill(0));
let dx = [-1,1,0,0];
let dy = [0,0,-1,1];

const masking = function(i, j) {
  let mask = `A${i}${j}`;

  let queue = [[i,j]];
  graph[i][j] = mask;
  
  while (queue.length > 0) {
    let [x, y] = queue.shift();
    
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (nx < 0 || nx >= len || ny < 0 || ny >= len) continue;
      if (graph[nx][ny] === 1 && visited[nx][ny] === 0) {
        visited[nx][ny] = 1;
        graph[nx][ny] = mask;
        queue.push([nx, ny]);
      }
    }
  }
  return;
}

const bfs = function(i, j, mask) {
  let queue = [[i,j]];
  visited[i][j] = 1;

  while (queue.length > 0) {
    let [x, y] = queue.shift();
    
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (nx < 0 || nx >= len || ny < 0 || ny >= len) continue;
      if (isNaN(graph[nx][ny]) && graph[nx][ny] !== mask) return visited[x][y] - 1;
      if (graph[nx][ny] === 0 && visited[nx][ny] === 0) {
        visited[nx][ny] = visited[x][y] + 1;
        queue.push([nx,ny]);
      }
    }
  }
  return Number.MAX_SAFE_INTEGER;
}

for (let i = 0; i < len; i++) {
  for (let j = 0; j< len; j++) {
    if (visited[i][j] === 0 && graph[i][j] === 1)
      masking(i, j);
  }
}
for (let i = 0; i < len; i++) {
  for (let j = 0; j < len; j++) {
    if (isNaN(graph[i][j]) && visited[i][j] === 0) {
      visited = Array.from(Array(len), () => Array(len).fill(0));
      bridge = Math.min(bridge, bfs(i, j, graph[i][j]));
    }
  }
}
console.log(bridge);
