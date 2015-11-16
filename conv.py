##### conv text list to list

#!/usr/bin/python

with open("conv-txt-list.py", "rb") as fp:
        lines = []
        for line in fp:
                #print len(line)
                if len(line) <> 1:
#                       if (line not in lines):
                                lines.append(line[:-1]) if line[-1] == "\n" else lines.append(line)
        print lines
