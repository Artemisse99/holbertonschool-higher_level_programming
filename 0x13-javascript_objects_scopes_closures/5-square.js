#!/usr/bin/node
class Rectangle {
    constructor(h, w) {
        if (h > 0 && w > 0){
        this.height = h;
        this.width = w;
        }else{
          return Rectangle.removeClass;
        }
      }

    print()
    {
        for(let i = 0; i < this.height; i++)
        {
            console.log('x'.repeat(this.height));
        }
        
    };
    rotate()
    {
        let temp = this.width
        this.width = this.height;
        this.height = temp;
    };
    double()
    {
        this.height *=2;
        this.width *=2;
        
    };
  };
  module.exports = class Square extends Rectangle
  {
    constructor(size) {
        super(size, size);
      }

  }