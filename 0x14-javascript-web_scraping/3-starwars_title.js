#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = baseUrl.concat(movieId);

request(fullUrl, (_err, response, body) => {
  const data = JSON.parse(body);
  console.log(data.title);
});
