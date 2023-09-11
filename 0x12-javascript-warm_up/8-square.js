#!/usr/bin/node
// a script that prints square of side n out of 'X' chars; n taken from first arg
const n = Math.floor(Number(process.argv[2]));
if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    let line = '';
    for (let a = 0; a < n; a++) {
      line = line + 'X';
    }
    console.log(line);
  }
}
