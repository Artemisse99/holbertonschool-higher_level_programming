#!/usr/bin/node
module.exports = class Rectangle {
  constructor (h, w) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    } else {
      return Rectangle.removeClass;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('x'.repeat(this.height));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
