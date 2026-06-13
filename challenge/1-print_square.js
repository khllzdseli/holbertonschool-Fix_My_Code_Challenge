#!/usr/bin/env node
/*
 * Prints a square with the character #
 */
if (process.argv.length <= 2) {
    process.stderr.write("Missing argument\n");
    process.exit(1);
}

const size = parseInt(process.argv[2], 10);
if (isNaN(size)) {
    process.stderr.write("Argument must be a number\n");
    process.exit(1);
}

for (let i = 0; i < size; i++) {
    let row = "";
    for (let j = 0; j < size; j++) {
        row += "#";
    }
    console.log(row);
}
