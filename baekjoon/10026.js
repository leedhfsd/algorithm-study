const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
const len = parseInt(input.shift());
const graph = input.map((v) => v.trim().split(''));

class Node {
  constructor(value, next = null) {
    this.value = value;
    this.next = next;
  }
}

class Queue {
  constructor() {
    this.length = 0;
    this.head = null;
    this.tail = null;
  }

  enqueue(value) {
    this.length++;
    if (this.length === 1) {
      this.head = this.tail = new Node(value);
      return;
    }
    const newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
  }

  dequeue() {
    this.length--; 
    const item = this.head.value;

    if (this.length === 0) {
      this.head = this.tail = null;
      return item;
    }
    this.head = this.head.next;
    return item;
  }
}
let visited = Array.from(Array(len), () => Array(len).fill(0));
let normal = 0;
let abnormal = 0;
const bfs = function(color, x, y) {
  let queue = new Queue();
  queue.enqueue([x, y]);
  let dx = [-1,1,0,0];
  let dy = [0,0,-1,1];

  while (queue.length > 0) {
    let [x, y] = queue.dequeue();
    for (let i = 0; i < 4; i++) {
      nx = x + dx[i];
      ny = y + dy[i];

      if (nx < 0 || nx >= len || ny < 0 || ny >= len) continue;
      if (graph[nx][ny] === color && visited[nx][ny] === 0) {
        visited[nx][ny] = 1;
        queue.enqueue([nx, ny]);
      }
    }
  }
}

//정상
for (let i = 0; i < len; i++) {
  for (let j = 0; j < len; j++) {
    if (visited[i][j] === 1) continue;
    if (graph[i][j] === "R") {
      bfs("R", i, j);
    } else if (graph[i][j] === "G") {
      bfs("G", i, j);
    } else if (graph[i][j] === "B") {
      bfs("B", i, j);
    }
    normal++;
  }
}

for (let i = 0; i < len; i++) {
  for (let j = 0; j < len; j++) {
    if (graph[i][j] === "G") {
      graph[i][j] = "R";
    }
  }
}
visited = Array.from(Array(len), () => Array(len).fill(0));

for (let i = 0; i < len; i++) {
  for (let j = 0; j < len; j++) {
    if (visited[i][j] === 1) continue;
    if (graph[i][j] === "R") {
      bfs("R", i, j);
    } else if (graph[i][j] === "B") {
      bfs("B", i, j);
    }
    abnormal++;
  }
}

console.log(normal, abnormal);
