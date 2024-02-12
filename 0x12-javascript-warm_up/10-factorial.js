#!/usr/bin/node
function facto (x) {
  if (isNaN(x)) {
    return (1);
  } else if (x === 0) {
    return (1);
  } else {
    const res = x * (facto(x - 1));
    return (res);
  }
}

const num = parseInt(process.argv[2]);
console.log(facto(num));
