#!/usr/bin/node
const fs = require('fs'); // CommonJS syntax
my_file = process.argv[2]
fs.readFile(my_file,'utf8',(err,data) =>
{ if (err){
    console.error(err);
    return;
}console.log(data)
});
