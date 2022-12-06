#!/usr/bin/node
const request = require('request');
url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`

request(url, (err, response, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
