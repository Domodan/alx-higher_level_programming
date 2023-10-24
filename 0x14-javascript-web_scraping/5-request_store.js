#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const fileName = process.argv[3];

request(url, (_err, response, body) => {
  const data = body;
  fs.writeFile(fileName, data, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
