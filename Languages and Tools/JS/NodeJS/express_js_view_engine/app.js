const express = require("express");
const app = express();

// Register View Engine (similar to flask jinja)
app.set("view engine", "ejs");
app.set("views", "templates"); // Default Views folder is /views; using templates instead

app.use(express.static(__dirname + "/static"));
app.listen(3000);

app.get("/", (req, res) => {
  const blogPosts = [
    {
      title: "First Post",
      body: "This is the body of the first blog post. It's brief and succinct.",
    },
    {
      title: "Second Post",
      body: "This is the body of the second blog post. It's also brief and succinct.",
    },
    {
      title: "Third Post",
      body: "This is the body of the third blog post. It's brief and succinct, too.",
    },
    {
      title: "Fourth Post",
      body: "This is the body of the fourth blog post. It's brief and succinct as well.",
    },
    {
      title: "Fifth Post",
      body: "This is the body of the fifth blog post. It's brief and succinct, just like the others.",
    },
  ];
  res.render("index", { title: "Home Page", blogPosts });
});

app.get("/about", (req, res) => {
  res.render("about", { title: "About Us" });
});

app.get("/about/", (req, res) => {
  res.redirect("about");
});

app.get("/create", (req, res) => {
  res.render("create", { title: "Create a Post" });
});

app.use((req, res) => {
  res.status(404).render("404", { title: "404: Not Found" });
});
