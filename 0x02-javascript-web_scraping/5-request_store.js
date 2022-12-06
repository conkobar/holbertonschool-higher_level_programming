#!/usr/bin/node
/* gets the contents of a webpage and stores it in a file */
const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Send a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) throw error;
  // Save the response body to a file
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) throw err;
  });
});
