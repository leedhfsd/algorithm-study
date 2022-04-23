//이 문제는 입력받는게 너무 어렵다..
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let len = 0;
const dx = [-1,1,0,0,0,0];
const dy = [0,0,-1,1,0,0];
const dz = [0,0,0,0,-1,1];
while (len !== input.length) {
  let [height, row, col] = [0,0,0];
  let queue = [];
  let flag = false;
  if (!isNaN(parseInt(input[len]))) {
    [height, row, col] = input[len].trim().split(' ').map(Number);
  }
  if (height === 0) break;
  len++;
  
  let graph = Array.from(Array(height), () => []);
  for (let i = 0; i < height; i++) {
    for (let j = len; j < len + row ; j++) {
      graph[i].push(input[j].trim().split(''));
    }
    len += row + 1;
  }
  for (let i = 0; i < height; i++) {
    for (let j = 0; j < row; j++) {
      for (let k = 0; k < col; k++) {
        if (graph[i][j][k] === "S") {
          queue.push([i,j,k]);
          graph[i][j][k] = 0;
          break;
        }
      }
    }
  }
  while (queue.length > 0) {
    if (flag) break;
    let [z, x, y] = queue.shift();
    for (let i = 0; i < 6; i++) {
      let nz = z + dz[i];
      let nx = x + dx[i];
      let ny = y + dy[i];
      
      if (nx < 0 || nx >= row || ny < 0 || ny >= col || nz < 0 || nz >= height) continue;
      if (graph[nz][nx][ny] === "#") continue;
      if (graph[nz][nx][ny] === "E") {
        flag = true;
        console.log(`Escaped in ${graph[z][x][y] + 1} minute(s).`);
      }
      if (graph[nz][nx][ny] === ".") {
        graph[nz][nx][ny] = graph[z][x][y] + 1;
        queue.push([nz,nx,ny]);
      } 
    }
  }
  !flag ? console.log("Trapped!") : "";
}
