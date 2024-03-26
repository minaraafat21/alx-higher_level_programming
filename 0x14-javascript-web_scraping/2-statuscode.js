#!/usr/bin/node
const request = require('request');
const my_url = process.argv[2];
request(my_url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
