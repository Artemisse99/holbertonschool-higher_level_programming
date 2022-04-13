#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv;
const url = args[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(args[3], body, 'utf8', function (err, data) { if (err) { console.log(err); } });
  }
});
