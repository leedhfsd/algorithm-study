const fs = require("fs");
const input = fs.readFileSync("text").toString().trim().split('\n').map(Number);
const testCase = input.shift();
let answer = '';
class Heap {
  constructor() {
    this.heap = [];
  }

  swap(index1, index2) {
    let temp = this.heap[index1];
    this.heap[index1] = this.heap[index2];
    this.heap[index2] = temp;
  }

  getParentIndex(index) {
    return Math.floor((index - 1) / 2) 
  }
  
  getLeftChildIndex(index) {
    return index * 2 + 1;
  }
  
  getRightChildIndex(index) {
    return index * 2 + 2;
  }
  
  getParentNode(index) {
    return this.heap[this.getParentIndex(index)];
  }

  getLeftChildNode(index) {
    return this.heap[this.getLeftChildIndex(index)];
  }

  getRightChildNode(index) {
    return this.heap[this.getRightChildIndex(index)];
  }
  
  peek() {
    return this.heap[0];
  }

  size() {
    return this.heap.length;
  }
  // 삽입한 마지막 원소를 맞는 위치에 조정
  bubbleUp() {
    let index = this.heap.length - 1;
    while (this.getParentIndex(index) !== undefined && this.getParentNode(index) > this.heap[index]) {
      this.swap(index, this.getParentIndex(index));
      index = this.getParentIndex(index);
    }
  } 
  // root node에서 꺼내는 경우 힙을 최소힙으로 만듦
  bubbleDown() {
    let index = 0;
    while (this.getLeftChildNode(index) !== undefined && 
          (this.getLeftChildNode(index) < this.heap[index] || 
          this.getRightChildNode(index) < this.heap[index])) {
            let smallIndex =  this.getLeftChildIndex(index);
            if (this.getRightChildNode(index) !== undefined && this.getRightChildNode(index) < this.heap[smallIndex]) {
              smallIndex = this.getRightChildIndex(index);
            }
            this.swap(index, smallIndex);
            index = smallIndex;
          }
  }

  add(item) {
    this.heap[this.heap.length] = item;
    this.bubbleUp();
  }

  delete() {
    let item = this.heap[0];
    this.heap[0] = this.heap[this.heap.length - 1];
    this.heap.pop();
    this.bubbleDown();
    return item;
  }

}
let minHeap = new Heap();
for (let i = 0 ; i < testCase; i++) {
  if (input[i] === 0) {
    if (minHeap.size() === 0) {
      answer += '0\n';
    } else {
      answer += `${minHeap.delete()}\n`;
    }
  }
  else {
    minHeap.add(input[i]);
  }
}
console.log(answer);
