#!/usr/bin/node

const argument = process.argv[2];

if (isNaN(argument)) {
  console.log("Not a number");
} else {
  const number = parseInt(argument, 10);
  console.log("My number:", number);
}
