#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (_err, response, body) => {
  console.log(`code: ${response.statusCode}`);
});
