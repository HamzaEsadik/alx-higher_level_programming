#!/usr/bin/node
const URL = process.argv[2];
const REQUEST = require('request');

REQUEST.get(URL, function (error, response, body) {
  console.log(response.statusCode);
});
