#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/', process.argv[2], (error, response, body) => {
  if (error) {
    console.error('error', error);
    
  }else{
    console.log('Code:', response.statusCode);
    }
});
