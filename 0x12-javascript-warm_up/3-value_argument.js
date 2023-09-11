#!/usr/bin/node
const firstArgument = process.argv[2];
const message = firstArgument !== undefined ? firstArgument : 'No argument';
console.log(message);
