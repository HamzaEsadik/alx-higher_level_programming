#!/usr/bin/node
const MOVIE_ID = process.argv[2];
const REQUEST = require('request');
const URL = 'https://swapi-api.alx-tools.com/api/films/' + MOVIE_ID;

REQUEST.get(URL, function (error, _, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
