## Description
# Checks
## File modes
## Shebang
## Nokogiri
## Invalid Formats
### CVE
### BID
### MSB
### MIL
### EDB
### US-CERT-VU
### ZDI
### URL
## Old Keywords
## Verbose
## Badchars
## File Extension
## Old Rubies
## Ranking
## Disclosure Date
## Title Casing
## Bad Terms
## Function Arguments
## Line Check
### Unicode
### Spaces at EOL
### Mixed Tab Spaces
### Tabs
### Carriage return
### File.open
### Load
### STDOUT
### Modified datastore
### Set-Cookie
### Auxiliary Rand
## Snake Case
## Old License
## VULN Codes
## vars_get
bad:
```ruby
res = send_request_raw({
  'uri' => uri_base + '/upload.php?type=file&folder=' + folder
})
```

good:
```ruby
res = send_request_raw({
  'uri' => uri_base + '/upload.php',
  'vars_get' => {
    'type' => 'file',
    'folder' => folder
  }
})
```

