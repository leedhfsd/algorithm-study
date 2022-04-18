// 연결리스트를 이용해서 Queue 간단하게 구현하기
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

  size() {
    return this.length;
  }
}

