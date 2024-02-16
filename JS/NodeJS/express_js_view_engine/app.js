const express = require("express");
const app = express();

// Register View Engine (similar to flask jinja)
app.set("view engine", "ejs");
app.set("views", "templates"); // Default Views folder is Views; using templates instead

app.use(express.static(__dirname + "/templates"));
app.listen(3000);

app.get("/", (req, res) => {
  res.render("index");
});

app.get("/about", (req, res) => {
  res.render("about");
});

app.get("/about/", (req, res) => {
  res.redirect("about");
});

app.use((req, res) => {
  res.status(404).render("404");
});