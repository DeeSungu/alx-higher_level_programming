#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// This is the first argument is the file path
const file = process.argv[2];
// The second argument is the string to write
const text = process.argv[3];
// The content of the file is written in utf-8
fs.writeFile(file, text, 'utf8', function (err, data) {
  // incase an error occurred during while writing, print the error object
  if (err) {
    console.log(err);
  }
});
