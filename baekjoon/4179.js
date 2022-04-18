const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

class Node {
  constructor(value, next = null) {
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
    const value = this.head.value;

    if (this.length === 0) {
      this.head = this.tail = null;
      return value;
    }

    this.head = this.head.next;
    return value;
  }

  size() {
    return this.length;
  }
}


const [row, col] = input.shift().trim().split(' ').map(Number);
let graph = [];
let Jvisited = Array.from(Array(row), () => Array(col).fill(0));
let Fvisited = Array.from(Array(row), () => Array(col).fill(0));
let Jqueue = new Queue();
let Fqueue = new Queue();
for (let i = 0; i < row; i++) {
  graph.push(input[i].trim().split(''));
}

for (let i = 0; i < row; i++) {
  for (let j = 0; j < col; j++) {
    if (graph[i][j] === "J") {
      Jqueue.enqueue([i,j]);
    } else if (graph[i][j] === "F") {
      Fqueue.enqueue([i, j]);
    }
  }
}

let dx = [-1,1,0,0];
let dy = [0,0,-1,1];
let index = 0;
while (Fqueue.length > 0) {
  let [x, y] = Fqueue.dequeue();
  for (let i = 0; i < 4; i++) {
    nx = x + dx[i];
    ny = y + dy[i];

    if (nx < 0 || nx >= row || ny < 0 || ny >= col) continue;
    if ((graph[nx][ny] === "J" || graph[nx][ny] === ".") && Fvisited[nx][ny] === 0) {
      Fvisited[nx][ny] = Fvisited[x][y] + 1;
      Fqueue.enqueue([nx, ny]);
    }
  }
}
index = 0;
let flag = false;
while (Jqueue.length > 0) {
  let [x, y] = Jqueue.dequeue();
  if (flag) break;
  for (let i = 0; i < 4; i++) {
    nx = x + dx[i];
    ny = y + dy[i];
    
    if (nx < 0 || nx >= row || ny < 0 || ny >= col) {
      console.log(Jvisited[x][y] + 1);
      flag = true;
      break;
    }
    if (Jvisited[nx][ny] > 0 || graph[nx][ny] === "#") continue;
    if (Fvisited[nx][ny] !== 0  && Fvisited[nx][ny] <= Jvisited[x][y] + 1) continue;
    Jvisited[nx][ny] = Jvisited[x][y] + 1;
    Jqueue.enqueue([nx, ny]);
  }
}
!flag ? console.log("IMPOSSIBLE") : "";
