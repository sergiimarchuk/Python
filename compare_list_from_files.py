#!/usr/bin/python
with open("out_list.txt", "rb") as list_out:
        for li in list_out:
                a = li,
                v=(((str(((str(a).split("'")))[1]).split("\\")))[0])
                with open("internal_list.txt", "rb") as intern_file:
                        for f in intern_file:
                                #v=(((str(((str(a).split("'")))[1]).split("\\")))[0])
                                if v in f:
                                        print
                                        print v," -| next out item consists in internal list. |- ",f,
