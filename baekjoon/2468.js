const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

class Node {
  constructor(value = value, next = null) {
    this.value = value;
    this.next = next;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
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


const len = parseInt(input.shift());
const graph = input.map((v) => v.trim().split(' ').map(Number));
let high = Number.MIN_SAFE_INTEGER;
let low = Number.MAX_SAFE_INTEGER;
let answer = Number.MIN_SAFE_INTEGER;
let dx = [-1,1,0,0];
let dy = [0,0,-1,1];
for (let i = 0; i < len; i++) {
  for (let j = 0; j < len; j++) {
    high = Math.max(high, graph[i][j]);
    low = Math.min(low, graph[i][j]);
  }
}

for (let i = low; i <= high; i++) {
  let visited = Array.from(Array(len), () => Array(len).fill(0));
  let queue = new Queue();
  let count = 0;
  for (let j = 0; j < len; j++) {
    for (let k = 0; k < len; k++) {
      if (graph[j][k] < i || visited[j][k] === 1) continue;
      queue.enqueue([j,k]);
      while (queue.length > 0){
        let [x, y] = queue.dequeue();
        for (let l = 0; l < 4; l++) {
          let nx = x + dx[l];
          let ny = y + dy[l];
  
          if (nx < 0 || nx >= len || ny < 0 || ny >= len) continue;
          if (graph[nx][ny] >= i && visited[nx][ny] === 0) {
            queue.enqueue([nx,ny]);
            visited[nx][ny] = 1;
          }
        }
      }
      count++;
    }
  }
  answer = Math.max(answer, count);
}
console.log(answer);
