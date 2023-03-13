#!/usr/bin/node
// Check the number of arguments passed to the script
if (process.argv.length === 2) {
    // If no arguments are passed, print "No argument"
    console.log('No argument');
} else if (process.argv.length === 3) {
    // If only one argument is passed, print "Argument found"
    console.log('Argument found');
} else {
    // If more than one argument is passed, print "Arguments found"
    console.log('Arguments found');
}
