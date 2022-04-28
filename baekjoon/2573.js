const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
const [row, col] = input.shift().trim().split(' ').map(Number);
const graph = input.map((v) => v.trim().split(' ').map(Number));
let dx = [-1, 1, 0, 0];
let dy = [0, 0, -1, 1];
let meltFlag = false;
let count = 0;
let answer = 0;

const meltBFS = function(i, j, graph, visited) {
  let queue = [[i, j]];
  visited[i][j] = 1;
  
  while (queue.length > 0) {
    let [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (graph[nx][ny] === 0 && visited[nx][ny] === 0 && graph[x][y] > 0) {
        graph[x][y] -= 1;
        continue;
      }

      if (graph[nx][ny] > 0 && visited[nx][ny] === 0) {
        queue.push([nx, ny]);
        visited[nx][ny] = 1;
      }
    }
  }
  return;
}

const bfs = function(x, y, graph, visited) {
  let queue = [[x,y]];
  visited[x][y] = 1;
  
  while (queue.length > 0) {
    let [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (nx < 0 || nx >= row || ny < 0 || ny >=col) continue;
      if (graph[nx][ny] > 0 && visited[nx][ny] === 0) {
        queue.push([nx, ny]);
        visited[nx][ny] = 1;
      }
    }
  }
  return;
}




while (count <= 1 && !meltFlag) {
  let visited = Array.from(Array(row), () => Array(col).fill(0));
  let visited1 = Array.from(Array(row), () => Array(col).fill(0));
  count = 0;
  let sum = 0;
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (graph[i][j] !== 0 && visited[i][j] === 0) {
        meltBFS(i, j, graph, visited);
      }
    }
  }

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (graph[i][j] !== 0 && visited1[i][j] === 0) {
        bfs(i, j, graph, visited1);
        count++;
      }
    }
  }

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      sum += graph[i][j];
    }
    if (sum > 0) break;
  }
  if (sum === 0) meltFlag = true;
  answer++;
}

meltFlag ? console.log(0) : console.log(answer);
