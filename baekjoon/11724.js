const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [vertex, edge] = input.shift().trim().split(' ').map(Number);
const visited = Array.from({length: 1001}, () => 0);
let count = 0;
let graph = {};
let keys = [];
for (let i = 0; i < edge; i++) {
  let [a, b] = input[i].trim().split(' ').map(Number);
  if (!keys.includes(a)) keys.push(a);
  if (!keys.includes(b)) keys.push(b);
  if (!graph[a]) {
    graph[a] = [b];
  } else {
    graph[a].push(b);
  }
  if (!graph[b]) {
    graph[b] = [a];
  } else {
    graph[b].push(a);
  }
}
const bfs = function(start) {
  let queue = [];
  queue.push(start);
  visited[start] = 1;

  while (queue.length > 0) {
    let x = queue.shift();
    for (let i = 0; i < graph[x].length; i++) {
      if (visited[graph[x][i]] === 0) {
        queue.push(graph[x][i]);
        visited[graph[x][i]] = 1;
      }
    }
  }
}

for (let i = 0; i < vertex; i++) {
  let node = keys[i];
  if (visited[node] === 0) {
    bfs(node);
    count++;
  }
}
let diff = vertex - Object.keys(graph).length;
console.log(count + diff);
