class Deque {
  constructor() {
    this.deque = [];
    this.front = 0;
    this.rear = 0;
    this.size = 10001;
    this.currentSize = 0;
    this.temp = 0;
  }
  mod(n, m) {
    return ((n % m) + m) % m;
  }
  isFull() {
    return (this.rear + 1) % this.size === this.front;
  }
  isEmpty() {
    return this.rear === this.front;
  }
  push_front(item) {
    if(!this.isFull()) {
      this.deque[this.front] = item;
      this.front = this.mod((this.front - 1),this.size);
      this.currentSize++;
    }
  } 
  push_back(item) {
    if(!this.isFull()) {
      this.rear = (this.rear + 1) % this.size;
      this.deque[this.rear] = item;
      this.currentSize++;
    }
  } 

  pop_front() {
    if(this.isEmpty()) {
      return -1;
    } else {
      this.front = (this.front + 1) % this.size;
      this.currentSize--;
      return this.deque[this.front];
    }
  }
  pop_back() {
    if(this.isEmpty()) {
      return -1;
    } else {
      this.currentSize--;
      this.temp = this.deque[this.rear];
      this.rear = (this.rear - 1 + this.size) % this.size;
      return this.temp;
    }
  }
  printSize() {
    return this.currentSize;
  }
  printFront() {
    if(this.isEmpty()) {
      return -1;
    } else {
      return this.deque[this.mod(this.front + 1, this.size)];
    }
  }
  printBack() {
    if(this.isEmpty()) {
      return -1;
    } else {
      return this.deque[this.rear];
    }
  }
}
