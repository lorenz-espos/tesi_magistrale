* **store_loot()** - Used to store both stolen files (both text and binary) and "screencaps" of commands such as a
```ps -ef```

and
```ifconfig```

* **report_host()** - Reports a host's liveness and attributes such as operating system and service pack. This is less common because other reporting methods already do this, such as
```report_service```

,
```report_exploit_success```

,
```report_client```

,
```report_note```

,
```report_host_tag```

,
```report_vuln```

,
```report_event```

,
```report_loot```

* **report_web_site()** - Reports a website, and must be tied to an existing
```:service```

. If there is no
```:service```

, you will have to supply
```:host```

,
```:port```

,
```:ssl```

* **report_loot()** - Very rarely, modules might actually want to export loots without using store_loot(). Typically they do this with Ruby's file IO, but this won't be logged in the database so can't be tracked by Metasploit Framework. In that case, a
```report_loot()```

is needed. However, 99.9% of the time you should be using
```store_loot()```

