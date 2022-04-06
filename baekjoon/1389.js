const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
let [vertex, edge] = input.shift().split(' ').map(Number);
let graph = {};
let result = Array.from({length: vertex + 1}, () => 0);
for (let i = 0; i < edge; i++) {
  let [a, b] = input[i].split(' ').map(Number);
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

const bfs = function(graph, start) {
  const visited = Array.from({length: vertex + 1}, () => 0);
  const queue = [[start, 0]];

  while (queue.length > 0) {
    let [node, count] = queue.shift();
    if (visited[node] === 0) {
      visited[node] = 1;
      result[start] += count++;
      graph[node].forEach((item) => queue.push([item, count]));
    }
  }
}

for (let i = 1; i <= vertex; i++) {
  bfs(graph, i);
}
result.shift();
console.log(result.indexOf(Math.min(...result)) + 1);
