#!/usr/bin/node
/** A square class that inherits from another square class*/
class Square extends require('./5-square.js'){
	 charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
