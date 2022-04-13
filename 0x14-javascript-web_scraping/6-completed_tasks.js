#!/usr/bin/node
const request = require('request');
const fargs = process.argv;
const url = fargs[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const js = JSON.parse(body);
    const dicto = {};
    for (const i of js) {
      if (i.completed === true) {
        if (dicto[i.userId] === undefined) {
          dicto[i.userId] = 0;
        }
        dicto[i.userId] += 1;
      }
    }
    console.log(dicto);
  }
});
