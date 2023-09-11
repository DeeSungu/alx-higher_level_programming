#!/usr/bin/node
// script that prints first arg passed to it, prints 'No argument' if no args
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
