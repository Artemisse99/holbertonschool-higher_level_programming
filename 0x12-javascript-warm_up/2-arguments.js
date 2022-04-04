#!/usr/bin/node
if (process.argv.lenghts < 3) {
  console.log('No argument');
} else if (process.argv.lengths === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
