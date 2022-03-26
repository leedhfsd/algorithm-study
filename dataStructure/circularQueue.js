class circularQueue {
  constructor(){
    this.queue = [];
    this.front = 0;
    this.rear = 0;
    this.size = 10000; 
  }

  isFull() {
    return (this.rear + 1) % this.size === this.front;
  }

  isEmpty() {
    return this.front === this.rear;
  }

  enqueue(item) {
    if (!this.isFull()) {
      this.rear = (this.rear + 1) % this.size;
      this.queue[this.rear] = item;
    }
  } 
  
  dequeue() {
    if (!this.isEmpty()){
      this.front = (this.front + 1) % this.size;
      return this.queue[this.front];
    } else if (this.isEmpty()) {
      return -1;
    }
  }

  printFront() {
    if (this.isEmpty()) {
      return -1;
    } else {
      return this.queue[this.front + 1];
    }
  }
  
  printBack() {
    if (this.isEmpty()) {
      return -1;
    } else {
      return this.queue[this.rear];
    }
  }

  printSize() {
    return this.rear - this.front;
  }
}
