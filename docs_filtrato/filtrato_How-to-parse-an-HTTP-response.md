## Getting a response
The following is an example of using the #send_request_cgi method from HttpClient:
```ruby
res = send_request_cgi({'uri'=>'/index.php'})
```

The return value for
```res```

## Getting the response body
With a Rex::Proto::Http::Response object, here's how you can retrieve the HTTP body:
```ruby
data = res.body
```

If you want to get the raw HTTP response (including the response message/code, headers, body, etc), then you can simply do:
```ruby
raw_res = res.to_s
```

However, in this documentation we are only focusing on
```res.body```

## Choosing the right parser
If the format you need to parse isn't on the list, then fall back to
```res.body```

## Parsing HTML with Nokogiri
When you have a Rex::Proto::Http::Response with HTML in it, the method to call is:
```ruby
html = res.get_html_document
```

Consider the following example as your HTML response:
```html
<html>
<head>
	<title>Hello, World!</title>
</head>
<body>
	<div class="greetings">
		<div id="english">Hello</div>
		<div id="spanish">Hola</div>
		<div id="french">Bonjour</div>
	</div>
</body>
<html>
```

If the #at method is used to find a DIV element:
```ruby
html = res.get_html_document
greeting = html.at('div')
```

Then the
```greeting```

variable should be a Nokogiri::XML::Element object that gives us this block of HTML (again, because the #at method only returns the first result):
```html
<div class="greetings">
<div id="english">Hello</div>
<div id="spanish">Hola</div>
<div id="french">Bonjour</div>
</div>
```

**Grabbing an element from a specific element tree**
```ruby
html = res.get_html_document
greeting = html.at('div//div')
```

Then the
```greeting```

variable should give us this block of HTML:
```html
<div id="english">Hello</div>
```

Let's say I don't want the English Hello, I want the Spanish one. Then we can do:
```ruby
html = res.get_html_document
greeting = html.at('div[@id="spanish"]')
```

Let's say I only know there's a DIV element that says "Bonjour", and I want to grab it, then I can do:
```ruby
html = res.get_html_document
greeting = html.at('//div[contains(text(), "Bonjour")]')
```

Or let's say I don't know what element the word "Bonjour" is in, then I can be a little vague about this:
```ruby
html = res.get_html_document
greeting = html.at('[text()*="Bonjour"]')
```

The #search method returns an array of elements. Let's say we want to find all the DIV elements, then here's how:
```ruby
html = res.get_html_document
divs = html.search('div')
```

When you have an element, you can always call the #text method to grab the text. For example:
```ruby
html = res.get_html_document
greeting = html.at('[text()*="Bonjour"]')
print_status(greeting.text)
```

The #text method can also be used as a trick to strip all the HTML tags:
```ruby
html = res.get_html_document
print_line(html.text)
```

The above will print:
```
"\n\nHello, World!\n\n\n\nHello\nHola\nBonjour\n\n\n" 
```

## Parsing XML
To get the XML body from Rex::Proto::Http::Response, do:
```ruby
xml = res.get_xml_document
```

## Parsing JSON
To get the JSON body from Rex::Proto::Http::Response, do:
```ruby
json = res.get_json_document
```

