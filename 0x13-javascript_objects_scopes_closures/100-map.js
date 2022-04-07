#!/usr/bin/node
let list = require('./100-map');
console.log(list);
let roots = list.map((num) => Math.sqrt(num));
console.log(roots);