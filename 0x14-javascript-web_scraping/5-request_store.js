#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

// Make a request to the URL
request(url, (err, res, body) => {
  if (err) {
    return console.error('Error making request:', err);
  }

  // Write the response body to a file
  fs.writeFile(file, body, 'utf8', (err) => {
    if (err) {
      return console.error('Error writing to file:', err);
    }
  });
});
