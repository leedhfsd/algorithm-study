const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const testCase = parseInt(input.shift())

const bfs = function(graph, visited, row, col) {
  let queue = [];
  let dx = [1,-1,-0,0];
  let dy = [0,0,-1,1];
  let group = [];
  
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      queue.push([i, j]);
      let count = 0;
      while (queue.length > 0) {
        let [x, y] = queue.pop();
        if (graph[x][y] === 1 && visited[x][y] === 0) {
          visited[x][y] = 1;
          count++;
          for (let k = 0; k < 4; k++) {
            nx = x + dx[k];
            ny = y + dy[k];
            if (nx < 0 || nx >= row || ny < 0 || ny >= col) continue;
            if (visited[nx][ny] === 0 && graph[nx][ny] === 1) {
              queue.push([nx, ny]);
            } 
          }
        }
      }
      count > 0 ? group.push(count) : "";
    }
  }
  return group;
}


for (let i = 0; i < testCase; i++) {
  let [col, row, count] = input.shift().split(' ').map(Number);
  let graph = Array.from(Array(row), () => Array(col).fill(0));
  let visited = Array.from(Array(row), () => Array(col).fill(0));
  for (let j = 0; j < count; j++) {
    let [x, y] = input.shift().split(' ').map(Number);
    graph[y][x] = 1;
  }
  console.log(bfs(graph, visited, row, col).length);
}
