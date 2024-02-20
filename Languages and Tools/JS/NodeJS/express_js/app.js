// Import the express module
const express = require("express");
//const fs = require("fs");

// Instantiate the Server Object
const app = express();

// Define Absolute Path
//const PATH = ".";

// Start Listening at Port 3000
app.listen(3000);

// Listening for Requests
// if we send a response to the browser, then we do not carry on with anymore of the code.

app.get("/", (req, res) => {
  // res.send("<p>test</p>");
  res.sendFile("./templates/index.html", { root: __dirname }); // We need an absolute path for sendFile
});

app.get("/about", (req, res) => {
  res.sendFile("./templates/about.html", { root: __dirname });
});

// Redirects
app.get("/about/", (req, res) => {
  res.redirect("/about");
});

// 404 page
// logical way of creating 404; if none of the other app.get's fire then this fires for every single request == if you don't find a page pretty much

app.use((req, res) => {
  res.status(404).sendFile("./templates/404.html", { root: __dirname });
});
