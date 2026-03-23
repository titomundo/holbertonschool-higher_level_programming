#!/usr/bin/node

const args = process.argv;

args.forEach((element, i) => {
  if (i > 1) {
    console.log(element);
  }
});
