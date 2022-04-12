#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let newlist = [];
    let match = '';
    newlist = Object.values(JSON.parse(body).results['0'].characters);
    newlist.forEach(element => {
      if (element.includes('18')) { match = element; }
    });
    request(match, function (error, response, body) {
      console.log((JSON.parse(body).films).length);
    }
    );
  }
});