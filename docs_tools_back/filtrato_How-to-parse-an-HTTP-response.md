`

**Basic usage of #at**

If the #at method is used to find a DIV element:

`

`

**Grabbing an element from a specific element tree**

`

`

**Grabbing an element with a specific attribute**

Let's say I don't want the English Hello, I want the Spanish one. Then we can do:

`

`

**Grabbing an element with a specific text**

Let's say I only know there's a DIV element that says "Bonjour", and I want to grab it, then I can do:

`

`

**Basic usage of #search**

The #search method returns an array of elements. Let's say we want to find all the DIV elements, then here's how:

`

`

**Accessing text**

When you have an element, you can always call the #text method to grab the text. For example:

`

`

If you actually want to keep the HTML tags, then instead of calling #text, call #inner_html.

**Accessing attributes**

With an element, simply call #attributes.

**Walking a DOM tree**

Use the #next method to move on to the next element.

Use the #previous method to roll back to the previous element.

Use the #parent method to find the parent element.

Use the #children method to get all the child elements.

Use the #traverse method for complex parsing.

## Parsing XML

To get the XML body from Rex::Proto::Http::Response, do:

`

