const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [row, col] = input.shift().trim().split(' ').map(Number);
let graph = [];
let visited = Array.from(Array(row), () => Array(col).fill(0));
let result = [];
for (let i = 0; i < row; i++) {
  graph.push(input[i].trim().split(' ').map(Number));
}

const bfs = function(a, b, visited) {
  let queue = [];
  queue.push([a, b]);
  visited[a][b] = 1;
  let index = 0;
  let count = 0;
  dx = [1,-1,0,0];
  dy = [0,0,-1,1];
  
  while (queue.length > index) {
    let [x, y] = queue[index++];
    
    for (let i = 0; i < 4; i++) {
      nx = x + dx[i];
      ny = y + dy[i];

      if (0 > nx || nx >= row || 0 > ny || ny >= col) continue;
      if (visited[nx][ny] === 0 && graph[nx][ny] === 1) {
        queue.push([nx, ny]);
        visited[nx][ny] = 1;
        count++;
      }
    }
  }
  return count + 1;
}

for (let i = 0; i < row; i++) {
  for (let j = 0; j < col; j++) {
    if (graph[i][j] === 1 && visited[i][j] === 0) {
      result.push(bfs(i, j, visited));
    }
  }
}
console.log(result.length);
result.length !== 0 ? console.log(Math.max(...result)) : console.log(0);
