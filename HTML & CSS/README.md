Hi hi, html stuff goes here

# HTML
**HTML** stands for **H**yper **T**ext **M**arkup **L**anguage. It is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.

## HTML Elements
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

# CSS Selectors
**Type Selectors** - Selects all elements of a specific type. For example, the following rule would apply to all <p> elements in the document: (Use the element name to select a type in css)
**Universal Selectors** - Selects all elements in the document. For example, the following rule would apply to all elements in the document: (Use * to select all elements in css)
**Class Selectors** - Selects all elements with a specific class attribute. For example, the following rule would apply to all elements with class="center": (Use . to select a class in css)
**ID Selectors** - Selects a single element with a specific id attribute. For example, the following rule would apply to the single element with id="intro": (Use # to select an id in css)
**Attribute Selectors** - Selects all elements with a specific attribute. For example, the following rule would apply to all elements with a title attribute (Use [] to select an attribute in css):