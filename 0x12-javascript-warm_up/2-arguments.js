#!/usr/bin/node
const numOfArgs = process.argv.length;
const message = numOfArgs === 0 ? 'No argument' : numOfArgs === 1 ? 'Argument found' : 'Arguments found';
console.log(message);
