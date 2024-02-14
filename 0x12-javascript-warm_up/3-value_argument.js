#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log("No argument");
} else {
  // Print the first argument passed to the script
  console.log(process.argv[2]);
}
