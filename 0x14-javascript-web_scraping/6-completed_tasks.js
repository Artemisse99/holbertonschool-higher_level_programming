#!/usr/bin/node
const request = require('request');
const fargs = process.argv;
const url = fargs[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const js = JSON.parse(body);
    const dic = {};
    for (const i of js) {
      if (i.completed === true) {
        if (dic[i.userId] === undefined) {
          dic[i.userId] = 0;
        }
        dic[i.userId] += 1;
      }
    }
    console.log(dic);
  }
});
