const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [row, col, height] = input.shift().trim().split(' ').map(Number);
let graph = Array.from(Array(height), () => Array(col).fill([]));
for (let i = 0; i < height; i++) {
  for (let j = 0; j < col; j++) {
    graph[i][j] = input.shift().trim().split(' ').map(Number);
  }
}
let queue = [];
for (let i = 0; i < height; i++){
  for (let j = 0; j < col; j++) {
    for (let k = 0; k < row; k++) {
      if (graph[i][j][k] === 1) {
        queue.push([i,j,k]);
      }
    }
  }
}
let index = 0;
let dx = [0,0,-1,1,0,0];
let dy = [1,-1,0,0,0,0];
let dz = [0,0,0,0,1,-1];

while (queue.length > index) {
  let [z, y, x] = queue[index++];
for (let i = 0; i < 6; i++){
    nz = z + dz[i];
    nx = x + dx[i];
    ny = y + dy[i];
      
    if (0 <= nz && nz < height && 0 <= nx && nx < row && 0 <= ny && ny < col) {
      if (graph[nz][ny][nx] === 0) {
        queue.push([nz,ny,nx]);
        graph[nz][ny][nx] = graph[z][y][x] + 1;
      }
    }
  }
}

let max = Number.MIN_SAFE_INTEGER;
let flag = false;
for (let i = 0; i < height; i++){
  if (flag) break;
  for (let j = 0; j < col; j++) {
    for (let k = 0; k < row; k++) {
      if (graph[i][j][k] === 0) {
        flag = true;
      }
      max = Math.max(max, graph[i][j][k]);
    }
  }
}

!flag ? console.log(max-1) : console.log(-1);
