#!/usr/bin/node
const URL = process.argv[2];
const REQUEST = require('request');

REQUEST.get(URL, function (response) {
  console.log('code: ' + response.statusCode);
});
