// Creating a object literal that references another module; can use it's methods and variables
const abc = require('./people');
console.log(abc.people);

// Essentially a composite literal; a dictionary that is of the shape of defined elements you are pulling from the required module
const { people, ages } = require('./people');
console.log(people, ages);

// Using the OS object
const os = require('os');

//console.log(os);
console.log(os.platform(), os.homedir());