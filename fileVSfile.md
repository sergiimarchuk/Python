<pre>
#!/usr/bin/python
with open("listacct.txt", "rb") as lfr:
        for l in lfr:
                a = l,
                with open("/etc/passwd", "rb") as pfr:
                        for f in pfr:
                                v=(((str(((str(a).split("'")))[1]).split("\\")))[0])
                                if v in f:
                                        print v,f
</pre>
