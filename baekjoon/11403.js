const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const length = parseInt(input.shift());
let graph = {};
let answer = '';
for (let i = 0; i < length; i++) {
  let node = input[i].trim().split(' ').map(Number);
  for (let j = 0; j < node.length; j++) {
    if (node[j] === 1) {
      if (!graph[i]) {
        graph[i] = [j];
      } else {
        graph[i].push(j);
      }
    }
  }
}

const dfs = function(vertex, visited) {
  let queue = [vertex];
  while (queue.length > 0) {
    let node = queue.shift();
    if (graph[node] === undefined) continue;
    for (let i = 0; i < graph[node].length; i++) {
      if (visited[graph[node][i]] === 0) {
        visited[graph[node][i]] = 1;
        queue = [graph[node][i],...queue];
      }
    }
  }
}

for (let i = 0; i < length; i++) {
  let visited = Array.from({length: length}, () => 0);
  dfs(i, visited);
  answer += `${visited.join(' ')}\n`;
}
console.log(answer);
