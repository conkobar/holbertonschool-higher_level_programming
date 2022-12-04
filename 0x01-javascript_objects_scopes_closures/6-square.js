#!/usr/bin/node
const OldSquare = require('./5-square');
module.exports = class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let x = 0; x < this.height; x++) {
      console.log(c.repeat(this.width));
    }
  }
};
