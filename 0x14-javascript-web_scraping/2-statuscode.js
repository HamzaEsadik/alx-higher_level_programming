#!/usr/bin/node
const URL = process.argv[2];
const REQUEST = require('request');

REQUEST.get(URL, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
