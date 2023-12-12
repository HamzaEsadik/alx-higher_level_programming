#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      let A = '';
      for (let i = 0; i < this.width; i++) {
        A += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(A);
      }
    }
  }
};
