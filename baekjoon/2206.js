//3차원 배열 선언하려고 애쓰지말고 그냥 2차원까지만 쓰자....
const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n');
const [row, col] = input.shift().trim().split(' ').map(Number);
const graph = input.map((v) => v.trim().split('').map(Number));

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
}


const bfs = function() {
  let queue = new Queue();
  let temp1 = Array.from(Array(row), () => Array(col).fill(0));
  let temp2 = Array.from(Array(row), () => Array(col).fill(0));
  let visited = [temp1,temp2];
  queue.enqueue([0,0,0]);
  visited[0][0][0] = visited[1][0][0] = 1;
  let dx = [-1,1,0,0];
  let dy = [0,0,-1,1];

  while (queue.length > 0) {
    let [broken, x, y] = queue.dequeue();
    if (x === row - 1 && y === col - 1) return visited[broken][row - 1][col - 1];

    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (0 > nx || nx >= row || 0 > ny || ny >= col) continue;
      if (graph[nx][ny] === 0 && visited[broken][nx][ny] === 0) {
        queue.enqueue([broken, nx, ny]);
        visited[broken][nx][ny] = visited[broken][x][y] + 1;
      }
      
      if (!broken && graph[nx][ny] === 1 && visited[1][nx][ny] === 0) {
        queue.enqueue([1, nx, ny]);
        visited[1][nx][ny] = visited[broken][x][y] + 1;
      }
    }
  }
  return -1;
}

console.log(bfs());
