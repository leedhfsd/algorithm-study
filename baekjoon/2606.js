const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const computer = parseInt(input.shift());
const edge = parseInt(input.shift());
let graph = {};
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

const dfs = function(graph) {
  let visited = [];
  let stack = [];
  if (!graph[1]) return 0;
  stack.push(1);
  while (stack.length > 0) {
    let vertex = stack.shift();
    if (!visited.includes(vertex)) {
      visited.push(vertex);
      stack = [...graph[vertex],...stack];
    }
  }
  return visited;
}
console.log(dfs(graph).length - 1);
