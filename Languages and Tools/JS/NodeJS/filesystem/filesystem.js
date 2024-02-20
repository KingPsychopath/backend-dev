// Import core module that we need to interact with the file system; this ability to interact with files isn't natively built into JS
const fs = require('fs');

// reading files (location of file, (function to fire after completed reading))
fs.readFile('./res/text.txt', (err, data) => { // Async function - (meaning it doesn't block code being procedurally run)
    if (err) {
        console.log(err);
    }
    //console.log(data); // Returns a buffer (package of data sent when we read the file)
    console.log(data.toString());
});

console.log('I am however crazy'); // Printed before the readFile function, because the readFile takes some time to do; it happens in it's own thread

// writing files
const thingToWrite = 'Hello, World!';
fs.writeFile('./res/writeFile.txt', thingToWrite, (err, data) => {
    if (err) {
        console.log(err);
    }
    console.log('File was written!');
})

// creating & deleting directories 
const folderName = 'assets'
if (!fs.existsSync(`./${folderName}`)) { 
    fs.mkdir(`./${folderName}`, (err) => {
        if (err) {
            console.log(err)
        }
        console.log(`Folder: ${folderName} created.`)
    });
}else{
    console.log(`Folder: ${folderName} already exists! Deleting it!`)
    fs.rmdir(`./${folderName}`, (err) => {
        if (err) {
            console.log(err);
        }
        console.log(`Folder: ${folderName} deleted!`)
    })
}

 
// deleting files
const fileName = 'writeFile.txt'
if(fs.existsSync(`./res/${fileName}`)) {
    fs.unlink(`./res/${fileName}`, (err) => {
        if (err) {
            console.log(err);
        }
        console.log(`File Deleted: ${fileName}`)
    })
}
