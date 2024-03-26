#!/usr/bin/node
const URL = process.argv[2];
const PATH = process.argv[3];
const REQUEST = require('request');
const FS = require('fs');

REQUEST(URL, function (error, _, body) {
  if (error) {
    console.log(error);
  } else {
    FS.writeFile(PATH, body, 'utf8', function (error) {
      if (error) {
        console.error(error);
      }
    });
  }
});
