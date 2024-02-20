// For reading large files (We can start using the data before it's fully been read)
// Analogy: Filling a pool
// You could fill a large tank and then deliver it to fill the pool, but that would involve waiting a long time and transporting such a large amount of water
// Streams, allow you to fill up a buffer with the data and deliver those chunks bits at a time for usage

const fs = require('fs');

const file = 'loremIpsum.txt'
const file2 = 'loremCopy.txt'
const file3 = 'loremCopyPipe.txt'
const readStream = fs.createReadStream(`./res/${file}`, {highWaterMark: 1024, encoding: 'utf8'});
// Data was originally small enough to be read in a single chunk so I decreased chunk size to 1024 bytes (1kb)
const writeStream = fs.createWriteStream(`./res/${file2}`)
const writeStream2 = fs.createWriteStream(`./res/${file3}`)


readStream.on('data', (chunk) => {
    console.log('--- NEW CHUNK ---');
    console.log(chunk.toString()); // not necessary when encoding in utf8
    console.log(chunk);
    writeStream.write('\n--- NEW CHUNK ---\n');
    writeStream.write(chunk);
});

// Piping - faster way of reading a stream and writing to a stream at the same time
readStream.pipe(writeStream2);

// Duplex streams (read and write to file at the same time)


