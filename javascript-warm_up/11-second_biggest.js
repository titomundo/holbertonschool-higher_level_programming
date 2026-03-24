#!/usr/bin/node

const args = process.argv;
args.splice(0, 2);

const list = args.map((n) => {
  return parseInt(n, 10);
});

list.sort((a, b) => {
  return a - b;
});

if (list.length < 2) {
  console.log(0);
} else {
  console.log(list[list.length - 2]);
}
