#!/usr/bin/node
const URL = process.argv[2];
const REQUEST = require('request');

REQUEST(URL, function (error, _, body) {
  let count = 0;
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    for (let i = 0; data.results[i] !== undefined; i++) {
      if (data.results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    }
    console.log(count);
  }
});
