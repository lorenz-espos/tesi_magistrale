## On this page
## List of supported reference identifiers 
CVE  | cvedetails.com |
```['CVE', '2014-9999']```

CWE | cwe.mitre.org |
```['CWE', '90']```

BID | securityfocus.com |
```['BID', '1234']```

MSB | technet.microsoft.com |
```['MSB', 'MS13-055']```

EDB | exploit-db.com |
```['EDB', '1337']```

US-CERT-VU | kb.cert.org |
```['US-CERT-VU', '800113']```

ZDI | zerodayinitiative.com |
```['ZDI', '10-123']```

WPVDB | wpvulndb.com |
```['WPVDB', '7615']```

PACKETSTORM | packetstormsecurity.com |
```['PACKETSTORM', '132721']```

URL | anything |
```['URL', 'http://example.com/blog.php?id=123']```

## Code example of references in a module

```ruby
class MetasploitModule < Msf::Exploit::Remote
  Rank = NormalRanking

  def initialize(info = {})
    super(
      update_info(
        info,
        'Name' => 'Code Example',
        'Description' => %q{
          This is an example of a module using references
        },
        'License' => MSF_LICENSE,
        'Author' => [ 'Unknown' ],
        'References' => [
          [ 'CVE', '2014-9999' ],
          ['BID', '1234'],
          ['URL', 'http://example.com/blog.php?id=123']
        ],
        'Platform' => 'win',
        'Targets' => [
          [ 'Example', { 'Ret' => 0x41414141 } ]
        ],
        'Payload' => {
          'BadChars' => "\x00"
        },
        'Privileged' => false,
        'DisclosureDate' => '2014-04-01',
        'DefaultTarget' => 0,
        'Notes' => {
          'AKA' => [ 'shellshock' ]
        }
      )
    )
  end

  def exploit
    print_debug('Hello, world')
  end

end
```

