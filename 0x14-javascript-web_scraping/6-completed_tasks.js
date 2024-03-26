#!/usr/bin/node
const REQUEST = require('request');
const url = process.argv[2];
REQUEST.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const DATA = JSON.parse(body);
    const completed = {};
    for (const x of DATA) {
      if (x.completed === true) {
        if (x.userId in completed) {
          completed[x.userId]++;
        } else {
          completed[x.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
