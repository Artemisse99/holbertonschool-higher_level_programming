#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return undefined;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('x'.repeat(this.weight));
    }
  }
}
module.exports = Rectangle;
