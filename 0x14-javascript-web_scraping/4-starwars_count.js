#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
let count = 0;
request(url, function (error, response, body) {
  if (response.statusCode !== 200) {
    console.log(error);
  } else {
    for (const values in JSON.parse(body).results) {
      JSON.parse(body).results[values].characters.forEach(element => {
        if (element.includes('18')) {
          count++;
        }
      });
    }
    console.log(count);
  }
});
