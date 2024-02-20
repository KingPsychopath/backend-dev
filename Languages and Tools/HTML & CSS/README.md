Hi hi, html stuff goes here

# HTML
**HTML** stands for **H**yper **T**ext **M**arkup **L**anguage. It is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.

## Syntax
HTML consists of a series of elements, which you use to enclose, or wrap, different parts of the content to make it appear a certain way, or act a certain way. The enclosing tags can make a word or image hyperlink to somewhere else, can italicize words, can make the font bigger or smaller, and so on.

**Tags** - The tags are used to define HTML elements. An HTML element usually consists of a start tag and end tag, with the content inserted in between:
```html
<tagname>Content goes here...</tagname>
```

Some Tags are self-closing, which means they don't have a closing tag. For example, the line break tag:
```html
<br>
```
It doesn't have a closing tag because it doesn't contain any content; a line break is just a line break; it doesn't contain anything.

**Attributes** - HTML elements can have attributes. Attributes provide additional information about the element. Attributes are always included in the start tag and are written in name/value pairs like: name="value".
```html
<tagname attribute="value">Content goes here...</tagname>
```

Attributes are used to provide additional information about HTML elements. They are always specified in the start tag and usually come in name/value pairs like: name="value".
They are unordered and case-insensitive. The attribute name and attribute value are case-insensitive, but the attribute value should be in quotes.

**Nested Elements** - HTML elements can be nested (elements can contain elements). All HTML documents consist of nested elements.
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>
  </body>
```
Here, the `<html>` element contains two other elements: `<head> `and `<body>`. The `<head>` element contains a `<title>` element, and the `<body>` element contains two other elements: `<h1>` and `<p>`.

Head and body are both children of the html element, and the title is a child of the head element. The h1 and p elements are children of the body element. The body is their parent.
Doctype is not an element, but a declaration. It is not a child of the html element, but a sibling (they are both children of the same parent).

# CSS
## Syntax
A CSS rule-set consists of a selector and a declaration block:
```css
selector {
  property: value;
  property: value;
  property: value;
  ...
}
```
The selector points to the HTML element you want to style. The declaration block contains one or more declarations separated by semicolons. Each declaration includes a CSS property name and a value, separated by a colon.

## Comments
Comments are used to explain the code and make it easier to understand. Comments are ignored by browsers. A CSS comment is placed inside the `/* */` delimiters.

```css
/* This is a single-line comment */
```

```css
/* This is
a multi-line
comment */
```

## Selectors
**Universal Selectors** - Selects all elements in the document. For example, the following rule would apply to all elements in the document: (Use * to select all elements in css)

**Type Selectors** - Selects all elements of a specific type. For example, the following rule would apply to all `<p>` elements in the document: (Use the element name to select a type in css)
```css
p {
  text-align: center;
  color: red;
}
```

**Class Selectors** - Selects all elements with a specific class attribute. For example, the following rule would apply to all elements with class="center": (Use . to select a class in css)
```css
.center {
  text-align: center;
  color: red;
}
```

**ID Selectors** - Selects a single element with a specific id attribute. For example, the following rule would apply to the single element with id="intro": (Use # to select an id in css)
```css
#intro {
  text-align: center;
  color: red;
}
```

**Attribute Selectors** - Selects all elements with a specific attribute. For example, the following rule would apply to all elements with a title attribute (Use [] to select an attribute in css):
```css
a[title] {
  background-color: yellow;
}
```

**Action Selectors** - Selects all elements that are in a specific state. For example, the following rule would apply to all elements that are being hovered over: (Use : to select an action in css)
```css
a:hover {
  background-color: yellow;
}
```

## Child Selectors
**Child/Descendant Selectors** - Selects all elements that are the children of a specified element. For example, the following rule would apply to all `<p>` elements that are children of a `<div>` element: (Use > to select a child in css)
```css
div > p {
  text-align: center;
  color: red;
}
```

While you can select all children of div with:
```css
div * {
  text-align: center;
  color: red;
}
```

**First Child Selectors** - Selects the first child element of a specified element. For example, the following rule would apply to the first child element of a `<div>` element: (Use :first-child to select the first child in css)
```css
div p:first-child {
  text-align: center;
  color: red;
}
```
Following the n-th child:
```css
div p:nth-child(2) {
  text-align: center;
  color: red;
}
```
## Colors
Colors are specified using predefined color names, RGB, HEX, HSL, RGBA, HSLA values.

**Color Names** - There are 140 color names supported by all browsers. For example, "red", "green", "blue", etc.

**RGB** - RGB values are specified with: rgb(red, green, blue). Each parameter (red, green, and blue) defines the intensity of the color as an integer between 0 and 255.

**HEX** - HEX values are specified with: #RRGGBB. The value of each color is represented by a 2-digit number. The values are 00 (lowest) to FF (highest).

**HSL** - HSL stands for Hue, Saturation, and Lightness. HSL values are specified with: hsl(hue, saturation, lightness). Hue is a degree on the color wheel (from 0 to 360). Saturation is a percentage 
value; 0% means a shade of gray and 100% is the full color. Lightness is also a percentage; 0% is black, 100% is white.

**RGBA** - RGBA values are specified with: rgba(red, green, blue, alpha). The alpha parameter is a number between 0.0 (fully transparent) and 1.0 (fully opaque).

**HSLA** - HSLA values are specified with: hsla(hue, saturation, lightness, alpha). The alpha parameter is a number between 0.0 (fully transparent) and 1.0 (fully opaque).

# JavaScript

See JS folder for more details, on javascript itself.
## Syntax

JavaScript is written in plain text, just like HTML and CSS, so you do not need any new tools to write a script. You can simply use any text editor (like Notepad) and save your file with a .html extension. HTML and JavaScript can be used in the same document.

JavaScript statements are composed of:
- Values, Operators, Expressions, Keywords, and Comments.
- Statements are separated by a semicolon.

To use JavaScript in an HTML document, you must include the external JavaScript file inside the HTML file. You can do this by using the `<script>` tag.

## Code within the head/body tag
```html
<!DOCTYPE html>
<html>
  <head>
    <script>
      function myFunction() {
        document.getElementById("demo").innerHTML = "Paragraph changed.";
      }
    </script>
  </head>
  <body>
    <h1>A Web Page</h1>
    <p id="demo">A Paragraph</p>
    <button type="button" onclick="myFunction()">Try it</button>
  </body>
</html>
```

# Code imported from an external file
```html
<!DOCTYPE html>
<html>
  <head>
    <script src="myScript.js"></script>
  </head>
  <body>
    <h1>A Web Page</h1>
    <p id="demo">A Paragraph</p>
    <button type="button" onclick="myFunction()">Try it</button>
  </body>
</html>
```

The external file (myScript.js) looks like this:
```javascript
    <!-- The external file (myScript.js) -->
    function myFunction() {
      document.getElementById("demo").innerHTML = "Paragraph changed.";
    }
```
    

## Comments
Comments can be used to explain JavaScript code, and to make it more readable. JavaScript comments can be used to explain JavaScript code, and to make it more readable. Comments can also be used to prevent execution, when testing alternative code.

**Single Line Comments** - Single line comments start with `//`. Any text between `//` and the end of the line will be ignored by JavaScript (will not be executed).

**Multi-line Comments** - Multi-line comments start with `/*` and end with `*/`. Any text between `/*` and `*/` will be ignored by JavaScript.
