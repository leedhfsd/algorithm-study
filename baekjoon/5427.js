const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
const testCase = parseInt(input.shift());
let dx = [-1, 1, 0, 0];
let dy = [0, 0, -1, 1];
let answer = '';

class Node {
  constructor(value = value, next) {
    this.value = value;
    this.next = null;
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
    this.tail.next  = newNode;
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

for (let i = 0; i < input.length; i++) {
  let [col ,row] = input[i].trim().split(' ').map(Number);
  let fVisited = Array.from(Array(row), () => Array(col).fill(0));
  let fQueue = new Queue();
  let sVisited = Array.from(Array(row), () => Array(col).fill(0));
  let sQueue = new Queue();
  let graph = [];
  let flag = false;
  for (let j = i + 1; j < i + row + 1; j++) {
    graph.push(input[j].trim().split(''));
  }
  for (let a = 0; a < row; a++) {
    for (let b = 0; b < col; b++) {
      if (graph[a][b] === "*") {
        fQueue.enqueue([a, b]);
      } else if (graph[a][b] === "@") {
        sQueue.enqueue([a, b]);
      }
    }
  }
  //불의 이동 계산 
  while (fQueue.length > 0) {
    let [fx, fy] = fQueue.dequeue();
    for (let k = 0; k < 4; k++) {
      let nfx = fx + dx[k];
      let nfy = fy + dy[k];

      if (nfx < 0 || nfx >= row || nfy < 0 || nfy >= col) continue;
      if (graph[nfx][nfy] === "@" || graph[nfx][nfy] === ".") {
        if (fVisited[nfx][nfy] === 0) {
          fVisited[nfx][nfy] = fVisited[fx][fy] + 1;
          fQueue.enqueue([nfx, nfy]);
        }
      }
    }
  }
  //상근이의 이동 계산
  while (sQueue.length > 0) {
    let [sx, sy] = sQueue.dequeue();
    if (flag) break;
    for (let k = 0; k < 4; k++) {
      let nsx = sx + dx[k];
      let nsy = sy + dy[k];
    
      if (nsx < 0 || nsx >= row || nsy < 0 || nsy >= col) {
        answer += `${sVisited[sx][sy] + 1}\n`;
        flag = true;
        break;
      }
      if (graph[nsx][nsy] === "#") continue;
      if (fVisited[nsx][nsy] !== 0 && sVisited[sx][sy] + 1 >= fVisited[nsx][nsy]) continue;
      if (graph[nsx][nsy] === "." && sVisited[nsx][nsy] === 0) {
        sVisited[nsx][nsy] = sVisited[sx][sy] + 1;
        sQueue.enqueue([nsx, nsy]);
      }
    }
  }
  !flag ? answer += "IMPOSSIBLE\n" : "";
  i = i + row;
}
console.log(answer);
