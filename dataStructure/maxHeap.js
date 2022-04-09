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
    return Math.floor((index - 1) / 2);
  }
  
  getLeftChildIndex(index) {
    return index * 2 + 1;
  }

  getRightChildIndex(index) {
    return index * 2 + 2;
  }

  getParent(index) {
    return this.heap[this.getParentIndex(index)];
  }

  getLeftChild(index) {
    return this.heap[this.getLeftChildIndex(index)];
  }

  getRightChild(index) {
    return this.heap[this.getRightChildIndex(index)];
  }

  peek() {
    return this.heap[0];
  }

  size() {
    return this.heap.length;
  }

  bubbleUp() {
    let index = this.heap.length - 1;
    while (this.getParent(index) !== undefined && this.heap[index] > this.getParent(index)) {
      this.swap(index, this.getParentIndex(index));
      index = this.getParentIndex(index);
    }
  }

  bubbleDown() {
    let index = 0;
    while (this.getLeftChild(index) !== undefined && 
          (this.getLeftChild(index) > this.heap[index] ||
           this.getRightChild(index) > this.heap[index])) {
            let largerIndex = this.getLeftChildIndex(index);
            // 오른쪽 자식 노드가 왼쪽 자식 노드보다 크다면 더 큰 쪽으로 swap을 한다
            if (this.getRightChild(index) !== undefined && this.getRightChild(index) > this.heap[largerIndex]) {
              largerIndex = this.getRightChildIndex(index);
            }
            this.swap(index, largerIndex);
            index = largerIndex;
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
