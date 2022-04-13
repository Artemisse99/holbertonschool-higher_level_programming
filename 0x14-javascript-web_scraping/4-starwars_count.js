#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obj = JSON.parse(body);
    const dictionary = {};
    for (const keys in obj) {
      if (obj[keys].completed === true) {
        dictionary[obj[keys].userId] = dictionary[obj[keys].userId] + 1 || 1;
      }
    }
    console.log(dictionary);
  }
});
