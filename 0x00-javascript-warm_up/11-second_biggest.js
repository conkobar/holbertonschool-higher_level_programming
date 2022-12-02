#!/usr/bin/node
function almostBig (arr) {
  let max = Math.max.apply(null, arr);
  arr.splice(arr.indexOf(max), 1);
  return Math.max.apply(null, arr);
}

if (process.argv[2]) {
  let dirt = process.argv
  const parsnip = dirt.map(function (arg) {
    return parseInt(arg);
  });
  console.log(almostBig(parsnip));
} else {
  console.log('0');
}
