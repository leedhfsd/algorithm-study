const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [row, col] = input.shift().split(' ').map(Number);

const graph = Array.from(Array(row), () => Array(col).fill(0));
const visited = Array.from(Array(row), () => Array(col).fill(0));
for (let i = 0; i < input.length; i++) {
  graph[i] = input[i].trim().split('').map(Number);
}

//bfs를 쓰는 이유는 bfs는 같은 레벨을 탐색한 후 다음 레벨을 탐색하기 때문임
const bfs = function (graph) {
  let queue = [];
  dx = [-1,1,0,0];
  dy = [0,0,-1,1];
  queue.push([0,0]);
  
  while (queue.length > 0) {
    let [x, y] = queue.shift();
    if (graph[x][y] >= 1 && visited[x][y] === 0) {
      visited[x][y] = 1;
      for (let i = 0; i < 4; i++) {
        nx = x + dx[i];
        ny = y + dy[i];
        if (nx < 0 || nx >= row || ny < 0 || ny >= col) continue;
        if (graph[nx][ny] === 1){
          graph[nx][ny] = graph[x][y] + 1;
          queue = [...queue, [nx,ny]];
        }
      }
    }
  }
}
bfs(graph);
console.log(graph[row-1][col-1]);
