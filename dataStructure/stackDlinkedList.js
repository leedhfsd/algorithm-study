//이중 연결 리스트로 간단하게 구현한 스택
class Node {
  constructor(value = null, prev = null, next = null) {
    this.value = value;
    this.prev = prev;
    this.next = next;
  }
}

class Stack {
  constructor() {
    this.length = 0;
    this.head = null;
    this.tail = null;
  }
  
  push(value) {
    this.length++;
    if (this.length === 1) {
      this.head = this.tail = new Node(value);
      return;
    }
    const newNode = new Node(value);
    let temp = new Node(null);
    this.tail.next = newNode;
    temp = this.tail;
    this.tail = newNode;
    this.tail.prev = temp;
  }

  pop() {
    this.length--;
    const value = this.tail.value;
    if (this.length === 0) {
      this.head = this.tail = null;
      return value;
    }
    this.tail = this.tail.prev;
    return value;
  }
  
  size() {
    return this.length;
  }
}
