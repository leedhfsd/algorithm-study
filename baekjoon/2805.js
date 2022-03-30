const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split('\n');
let n, m;
[n, m] = input[0].split(' ').map(Number);
const treeArr = input[1].split(' ').map(Number).sort((a, b) => a - b);

const binarySearch = (arr, target, start, end) => {

  let notTarget = Number.MIN_SAFE_INTEGER;
  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let sum = 0;
    
    arr.forEach((value) => {
      if (value - mid > 0) {
        sum += value - mid;
      }
    });
    if (sum === target) return mid;
    else if (sum > target) {
      start = mid + 1;
      notTarget = Math.max(mid, notTarget)
    } else if (sum < target) {
      end = mid - 1;
    }
  }
  return notTarget;
}

console.log(binarySearch(treeArr, m, 0, treeArr[n - 1]));
