const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
const [row, col, testCase] = input.shift().trim().split(' ').map(Number);
const graph = Array.from(Array(row), () => Array(col).fill(1));
const visited = Array.from(Array(row), () => Array(col).fill(0));
let result = [];
for (let i = 0; i < testCase; i++) {
  let [x1, y1, x2, y2] = input[i].trim().split(' ').map(Number);
  for (let j = y1; j < y2; j++) {
    for (let k = x1; k < x2; k++) {
      graph[j][k] = 0;
    }
  }
}

for (let i = 0; i < row; i++) {
  for (let j = 0; j < col; j++) {
    if (graph[i][j] === 1 && visited[i][j] === 0) {
      let queue = [];
      queue.push([i,j]);
      visited[i][j] = 1;
      let dx = [-1,1,0,0];
      let dy = [0,0,-1,1];
      let count = 0;

      while (queue.length > 0) {
        let [x, y] = queue.shift();
        count++;
        for (let i = 0; i < 4; i++) {
          nx = x + dx[i];
          ny = y + dy[i];

          if (0 > nx || nx >= row || 0 > ny || ny >= col) continue;
          if (graph[nx][ny] === 1 && visited[nx][ny] === 0) {
            queue.push([nx, ny]);
            visited[nx][ny] = 1;
          }
        }
      }
      result.push(count);
    }
  }
}
result.sort((a, b) => a - b);
console.log(result.length);
console.log(result.join(' '));
