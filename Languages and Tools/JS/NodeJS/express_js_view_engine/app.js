const express = require("express");
const app = express();

// Register View Engine (similar to flask jinja)
app.set("view engine", "ejs");
app.set("views", "templates"); // Default Views folder is /views; using templates instead

app.use(express.static(__dirname + "/static"));
app.listen(3005);

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
  res.render("layout", { title: "Home Page", body: "index", blogPosts });
});

app.get("/about", (req, res) => {
  res.render("layout", { title: "About Us", body: "about" });
});

app.get("/about/", (req, res) => {
  res.redirect("about");
});

app.get("/create", (req, res) => {
  res.render("layout", { title: "Create a Post", body: "create" });
});

app.use((req, res) => {
  res.status(404).render("layout", { title: "404: Not Found", body: "404" });
});
