#!/usr/bin/node
const dict = require('./101-data').dict;
const values = Object.values(dict);
const result = values.filter((item, index) => {
  return values.indexOf(item) === index;
});

const newDict = function (lista, dictionaty) {
  let i = 0;
  const endDict = {};
  while (i < lista.length) {
    const sublist = [];
    for (const key in dictionaty) {
      if (dictionaty[key] === lista[i]) {
        sublist.push(key);
      }
    }
    endDict[lista[i]] = sublist;
    i++;
  }
  return endDict;
};
console.log(newDict(result, dict));
