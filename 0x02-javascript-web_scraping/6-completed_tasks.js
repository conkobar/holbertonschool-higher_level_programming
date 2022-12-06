#!/usr/bin/node
/* computes the number of tasks completed by @userId */
const request = require('request');
const url = process.argv[2];

// send GET request to the specified URL
request.get(url, (err, response, body) => {
  if (err) throw err;
  const data = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (data[task.userId]) {
        data[task.userId]++;
      } else {
        data[task.userId] = 1;
      }
    }
  }
  console.log(data);
});
