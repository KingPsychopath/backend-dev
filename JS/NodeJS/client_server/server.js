const http = require("http");

// Could store the instance of the server as a variable (useful for websockets)
// createServer first argument, takes in a function that runs everytime a request is sent to the server.
const server = http.createServer((request, response) => {
  //console.log(request) // Returns - JSON Object of Request
  //console.log(`Request Made: ${request}`); // Returns - Stringified Object model i.e. Request Made: [object Object]
  console.log(`Request Made: ${request.url}, ${request.method}`); // Request Made: /, GET

  // Set Header Content Type for the Response
  //response.setHeader("Content-Type", "text/plain");
  response.setHeader("Content-Type", "text/html");

  // Returning HTML in line; preferably we would want to refer a separate HTML File
  response.write('<head><link rel="stylesheet.css" href="#"></head>');
  response.write("<h1>Hello, bro</h1>");
  response.write("<p> What is good bro!</p>");
  response.end();
});

// Server exists, but it is not actively listening for requests being sent to it; it just exists so we invoke the listen method

server.listen(3000, "localhost", () => {
  console.log("Listening for Requests on Port 3000");
}); // PORT, LOSTHOST(default), callbackfunction fires when we start listening
//127.0.0.1 = Loopback IP address
