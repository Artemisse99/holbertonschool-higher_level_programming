#!/usr/bin/node
const list = require('./100-map');
console.log(list);
const roots = list.map((num) => Math.sqrt(num));
console.log(roots);
