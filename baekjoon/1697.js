// 시간 최적화 필요함...
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(' ').map(Number);
let [a, b] = [input[0], input[1]];

const bfs = function(start, end) {
  let visited = Array.from({length: 100001}, () => 0);
  let timeArray = Array.from({length: 100001}, () => 0);
  let queue = [];
  queue.push([start, 0]);
  while (queue.length > 0) {
    let [point, time] = queue.shift();
    if (point === end) return time;
    if (visited[point] === 0 && point >= 0 && point <= 100000) {
      visited[point] = 1;
      timeArray[point] += time++;
      let nextStep = [point-1, point+1, point*2];
      if ((point-1 === end) || (point+1 === end) || (point*2 === end)) return time;
      nextStep.forEach((item) => {
        if (visited[item] === 0) {
          queue.push([item,time]);
        }
      })
    }
    
  }
}

console.log(bfs(a, b));
