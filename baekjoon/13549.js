const fs = require("fs");
const [a, b] = fs.readFileSync("/dev/stdin").toString().trim().split(' ').map(Number);
const visited = Array.from({length: 100001}, () => 0);
const bfs = function(a, b) {
  let queue = [[a, 0]];
  visited[a] = 1;
  let flag = false;
  let dx = [-1, 1];
  let index = 0;
  while (queue.length > index) {
    let i = 1;
    let [x, sec] = queue[index++];
    while (x * i <= 50000) {
      i = i * 2;
      if (x * i === b) {
        flag = true;
        break;
      }
      if (visited[x * i] === 0)
        queue.push([x * i, sec]);
    }
    if (flag) return sec;
    if (x === b) return sec;

    for (let i = 0; i < 2; i++) {
      let nx = x + dx[i];

      if (nx < 0 || nx > 100000 || visited[nx] === 1) continue;
      if (visited[nx] === 0) {
        queue.push([nx, sec + 1]);
        visited[nx] = 1;
      }
    }
  }
  return;
} 
console.log(bfs(a, b));
