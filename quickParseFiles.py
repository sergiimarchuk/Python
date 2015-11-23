""" after reun command via ssh on sevarl hosts do parse csv file """
# cat e.py
$ cat parse.py 
#!/usr/bin/python

text_file = open("logname2015-11_8-9-53.csv", "r")
lines = text_file.readlines()
counter = 0
for line in lines:
    counter = counter +1
    v0 = (line).split("[\'")[1]
    v1 = (v0).split("\\n\']")[0]
    #print "Hostname - v1 "+str(counter)+"-  ",v1
    v2 = (line).split("[\'")[2]
    #print 'v2: ',v2
    v3 = (v2).split("\\n\']")[0]
    #print 'v3 :', v3
    print v1+v3
