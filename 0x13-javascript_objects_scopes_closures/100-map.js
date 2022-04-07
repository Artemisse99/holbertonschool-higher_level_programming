#!/usr/bin/node
let list = require('./100-data').list;
console.log(list);
let roots = list.map((num, index) => num * index);
console.log(roots);
