#!/usr/bin/node
const fs = require("fs"); // CommonJS syntax
my_file = process.argv[2];
fs.readFile(my_file, "utf8", function (err, data) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
