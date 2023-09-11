#!/usr/bin/node
const argument1 = process.argv[2];
const number = parseInt(argument1);
message = !isNaN(number) ? `My number: ${number}` : "Not a number";
console.log(message);
