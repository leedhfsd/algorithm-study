class stack{
  constructor(){
    this.stack = [];
    this.top = -1;
    this.size = 10000;
    this.temp = 0;
  }

  isFull() {
    return this.top === this.size - 1;
  }

  isEmpty() {
    return this.top === -1;
  }

  push(item) {
    if (!this.isFull()) {
      this.top += 1;
      this.stack[this.top] = item;
    }
  } 
  
  pop() {
    if (!this.isEmpty()){
      this.temp = this.stack[this.top];
      this.top -= 1;
      return this.temp;
    } else if (this.isEmpty()) {
      return -1;
    }
  }
  
  printTop() {
    if (this.isEmpty()) {
      return -1;
    } else {
      return this.stack[this.top];
    }
  }

  printSize() {
    return this.top + 1;
  }
}
