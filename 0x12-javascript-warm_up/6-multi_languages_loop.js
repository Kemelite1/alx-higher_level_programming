#!/usr/bin/node
const threeLines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (let i = 0; i < threeLines.length; i++){
	process.stdout.write(threeLines[i] + '\n');
}
