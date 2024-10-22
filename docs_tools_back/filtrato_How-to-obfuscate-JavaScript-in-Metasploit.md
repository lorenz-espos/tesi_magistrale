Stealth is an important feature to think about during exploit development. If your exploit gets caught all the time, it doesn't matter how awesome or how technically challenging your exploit is, it is most likely not very usable in a real penetration test. Browser exploits in particular, heavily rely on JavaScript to trigger vulnerabilities, therefore a lot of antivirus or signature-based intrusion detection/prevention systems will scan the JavaScript and flag specific lines as malicious. The following code used to be considered as MS12-063 by multiple [antivirus vendors](https://www.virustotal.com/en/file/90fdf2beab48cf3c269f70d8c9cf7736f3442430ea023d06b65ff073f724870e/analysis/1388888489/) even though it is not necessarily harmful or malicious, we'll use this as an example throughout the wiki:
```
$ ./msfconsole -q
msf > irb
[*] Starting IRB shell...

>> 
```

In Metasploit, there are three common ways to obfuscate your JavaScript. The first one is simply by using the
```
>> obfu.obfuscate('Symbols' => {'Variables'=>['arrr']}, 'Strings' => true)
=> "\nvar QqLFS = new Array();\nQqLFS[0] = windows.document.createElement(unescape(String.fromCharCode(  37, 54, 071, 045, 0x36, 0144, 37, 066, 067 )));\nQqLFS[0][String.fromCharCode(  115, 0x72, 0143 )] = unescape(String.fromCharCode(  045, 0x36, 0x31 ));\n"
```

## The rand_text_alpha trick
Using
```
$ ./msfconsole -q
msf > irb
[*] Starting IRB shell...

>> 
```

By using the above MS12-063, here's how you would use
```
>> js = ::Rex::Exploitation::JSObfu.new %Q|alert('hello, world!');|
=> alert('hello, world!');
>> js.obfuscate
=> nil
```

:
```ruby
>> js = ::Rex::Exploitation::JSObfu.new %Q|function test() { alert("hello"); }|
=> function test() {
  alert("hello");
}
>> js.obfuscate
```

## The ObfuscateJS class
The ObfuscateJS class is like the
```ruby
>> puts js.sym("test")
_
```

technique on steroids, but even better. It allows you to replace symbol names such as variables, methods, classes, and namespaces. It can also obfuscate strings by either randomly using
```
>> puts js
function _(){window[(function () { var N="t",r="r",i="ale"; return i+r+N })()](String.fromCharCode(0150,0x65,0154,0x6c,0x6f));}
```

or
```
>> js = ::Rex::Exploitation::JSObfu.new %Q|alert('hello, world!');|
=> alert('hello, world!');
>> js.obfuscate(:iterations=>3)
=> window[String[((function(){var s=(function () { var r="e"; return r })(),Q=(function () { var I="d",dG="o"; return dG+I })(),c=String.fromCharCode(0x66,114),w=(function () { var i="C",v="r",f="omCh",j="a"; return f+j+v+i })();return c+w+Q+s;})())](('Urx'.length*((0x1*(01*(1*020+5)+1)+3)*'u'.length+('SGgdrAJ'.length-7))+(('Iac'.length*'XLR'.length+2)*'qm'.length+0)),(('l'.length*((function () { var vZ='k'; return vZ })()[((function () { var E="h",t="t",O="leng"; return O+t+E })())]*(0x12*1+0)+'xE'.length)+'h'.length)*(function () { var Z='uA',J='tR',D='x'; return D+J+Z })()[((function () { var m="th",o="g",U="l",Y="en"; return U+Y+o+m })())]+'lLc'.length),('mQ'.length*(02*023+2)+('Tt'.length*'OEzGiMVf'.length+5)),(String.fromCharCode(0x48,0131)[((function () { var i="gth",r="len"; return r+i })())]*('E'.length*0x21+19)+(0x1*'XlhgGJ'.length+4)),(String.fromCharCode(0x69)[((function () { var L="th",Q="n",$="l",I="g",x="e"; return $+x+Q+I+L })())]*('QC'.length*0x2b+3)+(01*26+1)))]((function(){var C=String[((function () { var w="rCode",j="mCha",A="fr",B="o"; return A+B+j+w })())]((6*0x10+15),('riHey'.length*('NHnex'.length*0x4+2)+4),(01*95+13),(1*('Z'.length*(0x1*(01*(0x3*6+5)+1)+18)+12)+46),(0x1*(01*013+6)+16)),JQ=String[((function () { var NO="ode",T="rC",HT="fromCha"; return HT+T+NO })())](('J'.length*0x54+17),(0x2*051+26),('TFJAGR'.length*('ymYaSJtR'.length*'gv'.length+0)+12),(01*0155+2),(0xe*'FBc'.length+2),(0x1*22+10),(3*(01*043+1)+11)),g=(function(){var N=(function () { var s='h'; return s })();return N;})();return g+JQ+C;})());
```

`
$ ./msfconsole -q
msf > irb
[*] Starting IRB shell...

>> 
`

`
>> obfu.obfuscate('Symbols' => {'Variables'=>['arrr']}, 'Strings' => true)
=> "\nvar QqLFS = new Array();\nQqLFS[0] = windows.document.createElement(unescape(String.fromCharCode(  37, 54, 071, 045, 0x36, 0144, 37, 066, 067 )));\nQqLFS[0][String.fromCharCode(  115, 0x72, 0143 )] = unescape(String.fromCharCode(  045, 0x36, 0x31 ));\n"
`

`

## The JSObfu class

The JSObfu class used to be ObfuscateJS' cousin, but it has been completely rewritten since September 2014, and packaged as a [gem](https://rubygems.org/gems/jsobfu). The obfuscation is more complex and you can actually tell it to obfuscate multiple times. You also no longer have to manually specify what symbol names to change, it just knows.

**Trying JSObfu in Rex**

Let's get back to irb again to demonstrate how easy it is to use JSObfu:

`

`
$ ./msfconsole -q
msf > irb
[*] Starting IRB shell...

>> 
`

`
>> js = ::Rex::Exploitation::JSObfu.new %Q|alert('hello, world!');|
=> alert('hello, world!');
>> js.obfuscate
=> nil
`

`ruby
>> js = ::Rex::Exploitation::JSObfu.new %Q|function test() { alert("hello"); }|
=> function test() {
  alert("hello");
}
>> js.obfuscate
`

`ruby
>> puts js.sym("test")
_
`

`
>> puts js
function _(){window[(function () { var N="t",r="r",i="ale"; return i+r+N })()](String.fromCharCode(0150,0x65,0154,0x6c,0x6f));}
`

`
>> js = ::Rex::Exploitation::JSObfu.new %Q|alert('hello, world!');|
=> alert('hello, world!');
>> js.obfuscate(:iterations=>3)
=> window[String[((function(){var s=(function () { var r="e"; return r })(),Q=(function () { var I="d",dG="o"; return dG+I })(),c=String.fromCharCode(0x66,114),w=(function () { var i="C",v="r",f="omCh",j="a"; return f+j+v+i })();return c+w+Q+s;})())](('Urx'.length*((0x1*(01*(1*020+5)+1)+3)*'u'.length+('SGgdrAJ'.length-7))+(('Iac'.length*'XLR'.length+2)*'qm'.length+0)),(('l'.length*((function () { var vZ='k'; return vZ })()[((function () { var E="h",t="t",O="leng"; return O+t+E })())]*(0x12*1+0)+'xE'.length)+'h'.length)*(function () { var Z='uA',J='tR',D='x'; return D+J+Z })()[((function () { var m="th",o="g",U="l",Y="en"; return U+Y+o+m })())]+'lLc'.length),('mQ'.length*(02*023+2)+('Tt'.length*'OEzGiMVf'.length+5)),(String.fromCharCode(0x48,0131)[((function () { var i="gth",r="len"; return r+i })())]*('E'.length*0x21+19)+(0x1*'XlhgGJ'.length+4)),(String.fromCharCode(0x69)[((function () { var L="th",Q="n",$="l",I="g",x="e"; return $+x+Q+I+L })())]*('QC'.length*0x2b+3)+(01*26+1)))]((function(){var C=String[((function () { var w="rCode",j="mCha",A="fr",B="o"; return A+B+j+w })())]((6*0x10+15),('riHey'.length*('NHnex'.length*0x4+2)+4),(01*95+13),(1*('Z'.length*(0x1*(01*(0x3*6+5)+1)+18)+12)+46),(0x1*(01*013+6)+16)),JQ=String[((function () { var NO="ode",T="rC",HT="fromCha"; return HT+T+NO })())](('J'.length*0x54+17),(0x2*051+26),('TFJAGR'.length*('ymYaSJtR'.length*'gv'.length+0)+12),(01*0155+2),(0xe*'FBc'.length+2),(0x1*22+10),(3*(01*043+1)+11)),g=(function(){var N=(function () { var s='h'; return s })();return N;})();return g+JQ+C;})());
`

`

**Using JSObfu for module development**

When you are writing a module, you should not call Rex directly like the above examples. Instead, you should be using the `

