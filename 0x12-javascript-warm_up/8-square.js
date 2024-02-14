#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
    console.log('Missing size');
  } else {
    const x = Number(process.argv[2]);
    let i = 0;
    let j = 0;
    while (i < x) {
        j = 0;
        while (j < x) {
            process.stdout.write('X');
            j++;
        }
        console.log();
      i++;
    }
  }
