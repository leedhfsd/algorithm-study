const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const length = parseInt(input.shift());
const graph = [];
let visited = Array.from(Array(length), () => Array(length).fill(0));
for (let i = 0; i < input.length; i++) {
  graph.push(input[i].split('').map(Number));
}

const bfs = function(graph, visited) {
  let queue = [];
  let group = [];
  let dx = [0,0,-1,1];
  let dy = [1,-1,0,0,];
  
  for (let i = 0; i < graph.length; i++) {
    for (let j = 0; j < graph.length; j++) {
      queue.push([i,j]);
      let count = 0;
      while (queue.length > 0) {
        let [x, y] = queue.pop();
        if (visited[x][y] === 0 && graph[x][y] === 1) {
          visited[x][y] = 1;
          count++;
          for (let k = 0; k < 4; k++) {
            nx = x + dx[k];
            ny = y + dy[k];
            if (nx < 0 || nx >= length || ny < 0 || ny >=length) continue;
            if (visited[nx][ny] === 0 && graph[nx][ny] === 1) {
              queue.push([nx,ny]);
            }
          }
        }
      }
      count !== 0 ? group.push(count) : "";
    }
  }
  return group.sort((a, b) => a -b);
}

let answer = bfs(graph, visited);
console.log(answer.length);
console.log(answer.join('\n'));
