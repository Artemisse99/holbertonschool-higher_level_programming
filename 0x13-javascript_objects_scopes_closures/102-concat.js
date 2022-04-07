#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const fileA = fs.readFileSync(args[2], 'utf8');
const fileB = fs.readFileSync(args[3], 'utf8');
fs.writeFile(args[4], fileA + fileB, 'utf8', function (err, data) { if (err) { console.log(err); } });
