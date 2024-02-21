Yes, there is a more tidy syntax similar to Jinja2 in Flask, which is achieved by using the `express-ejs-layouts` package in Node.js. This package allows you to create a main layout file and then extend it in your other views, similar to how you would in Flask with Jinja2.

Here's how you can do it:

1. First, install the `express-ejs-layouts` package:

```bash
npm install express-ejs-layouts
```

2. Then, in your main server file (usually `app.js` or `server.js`), require and use the package:

```javascript
const expressLayouts = require("express-ejs-layouts");

app.set("view engine", "ejs");
app.use(expressLayouts);
```

3. Create a new EJS file, let's call it `layout.ejs`, and put the common HTML structure there. You can use `<%- body %>` as a placeholder for where the specific page content will go:

```html
<!-- layout.ejs -->
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title><%- title %></title>
    <link rel="stylesheet" href="styles.css" />
  </head>

  <body>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/blogs/create">Blog</a></li>
      </ul>
    </nav>
    <div class="content"><%- body %></div>
  </body>
</html>
```

4. In your specific page EJS files, you can then extend this layout and provide the specific content. Here's an example with your `404.ejs`:

```html
<!-- 404.ejs -->
<% layout('layout') %> <% title = '404 Page' %>

<div class="not-found">
  <h1>404 Page Not Found</h1>
  <p>The page you are looking for does not exist.</p>
</div>
```

In this example, the `layout('layout')` statement tells EJS to use the `layout.ejs` file as the layout for this view. The `title` variable is defined and then used in the `layout.ejs` file. The rest of the `404.ejs` file is the specific content for this view.

# Learned

In EJS, `<%`, `<%=` and `<%-` have different uses:

- `<% code %>`: This tag is used to embed any JavaScript code into the EJS template. The code inside these tags is executed, but nothing is output into the template, this is typically used for variable assignments or control flow.

- <%= %> is used to output the result of JavaScript code into the template. The difference between <%= %> and <%- %> is that <%= %> escapes any HTML characters.

- `<%- code %>`: This tag is also used to embed JavaScript code, but it outputs the result directly into the template. This is used when you want to output HTML or any other type of content that shouldn't be escaped.

For example, if you have a variable `var htmlContent = "<p>Hello, world!</p>";`, you can output it into your template like this:

```ejs
<%- htmlContent %>
```

This will output the HTML as is, and you'll see "Hello, world!" in a paragraph in your rendered HTML. If you used `<%= htmlContent %>`, the HTML tags would be escaped and you'd see the literal string "<p>Hello, world!</p>" in your rendered HTML.

```ejs
<%= htmlContent %>
```

This will escape the HTML tags, and you'll see the literal string "<p>Hello, world!</p>" in your rendered HTML. If you used <%- message %>, the HTML tags would not be escaped and you'd see "Hello, world!" in a paragraph in your rendered HTML.
