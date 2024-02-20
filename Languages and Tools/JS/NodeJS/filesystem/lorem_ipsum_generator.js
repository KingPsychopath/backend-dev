// requirements - npm install lorem-ipsum
const fs = require('fs');
const { loremIpsum } = require('lorem-ipsum');

const text = loremIpsum({
  count: 100,             // Number of "words", "sentences", or "paragraphs"
  format: "plain",        // "plain" or "html"
  paragraphLowerBound: 3, // Min. number of sentences per paragraph.
  paragraphUpperBound: 7, // Max. number of sentences per para.
  random: Math.random,    // A PRNG function
  sentenceLowerBound: 5,  // Min. number of words per sentence.
  sentenceUpperBound: 15, // Max. number of words per sentence.
  units: "paragraphs"     // paragraph(s), "sentence(s)", or "word(s)"
});

fs.writeFileSync('loremIpsum.txt', text);