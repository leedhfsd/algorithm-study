const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
const [col, row] = input.shift().trim().split(' ').map(Number);
let graph = [];
let index = 0;
for (let i = 0; i < row; i++) {
  graph.push(input[i].trim().split(' ').map(Number));
}
let queue = [];

for (let i = 0; i < row; i++) {
  for (let j = 0; j < col; j++) {
    if (graph[i][j] === 1) {
      queue.push([i, j]);
    }
  }
}
console.log(graph);
let dx = [1, -1, 0, 0];
let dy = [0, 0, -1, 1];

while (queue.length > index) {
  let [x, y] = queue[index++];
  for (let i = 0; i < 4; i++) {
    nx = x + dx[i];
    ny = y + dy[i];
    if (0 <= nx && nx < row && 0 <= ny && ny < col) {
      if (graph[nx][ny] == 0){
        graph[nx][ny] = graph[x][y] + 1;
        queue.push([nx, ny]);
      }
    }
  }
}



let flag = true;
let days = Number.MIN_SAFE_INTEGER;
graph.forEach((arr) => {
  if (arr.includes(0)) {
    flag = false;
  }
  days = Math.max(...arr, days);
})
if (days === -1) days = 1;
flag ? console.log(days - 1) : console.log(-1);
