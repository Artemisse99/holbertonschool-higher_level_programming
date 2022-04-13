#!/usr/bin/node
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[2], 'utf8', (err, data) => {
  if (err) throw err;
});
