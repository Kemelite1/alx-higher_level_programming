#!/usr/bin/node
const number = Math.floor(Number(process.argv[2]));
const message = isNaN(number) ? 'Not a number' : `My number: ${number}`;
console.log(message);
