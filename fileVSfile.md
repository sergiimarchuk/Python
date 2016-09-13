```python
#!/usr/bin/python
with open("listacct.txt", "rb") as lfr:
        for l in lfr:
                a = l,
                with open("/etc/passwd", "rb") as pfr:
                        for f in pfr:
                                v=(((str(((str(a).split("'")))[1]).split("\\")))[0])
                                if v in f:
                                        print v,f
```

```python
#!/usr/bin/python
with open("listacct.txt", "rb") as list_account:
        for li in list_account:
                a = li,
                v=(((str(((str(a).split("'")))[1]).split("\\")))[0])
                with open("/etc/passwd", "rb") as pass_file:
                        for f in pass_file:
                                #v=(((str(((str(a).split("'")))[1]).split("\\")))[0])
                                if v in f:
                                        print
                                        print v," -| next account consists previous pattern. |- ",f
```
