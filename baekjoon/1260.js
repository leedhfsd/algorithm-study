const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const [vertex, edge, start] = input.shift().split(' ').map(Number);
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
    graph[b]. push(a);
  }
  graph[a].sort((a, b) => a - b);
  graph[b].sort((a, b) => a - b);
}

const dfs = function(start) {
  let visited = [];
  let stack = [];
  stack.push(start);

  while (stack.length > 0 ) {
    let vertex = stack.shift();
    if (!visited.includes(vertex)) {
      visited.push(vertex);
      if(graph[vertex])
        stack = [...graph[vertex], ...stack];
    }
  }
  return visited;
};
const bfs = function(start) {
  let visited = [];
  let queue = [];
  queue.push(start);

  while (queue.length > 0) {
    let vertex = queue.shift();
    if (!visited.includes(vertex)) {
      visited.push(vertex);
      if(graph[vertex])
        queue = [...queue, ...graph[vertex]];
    } 
  }
  return visited;
}

console.log(dfs(start).join(' '));
console.log(bfs(start).join(' '));
