```python
lis = [0,3,4,3,5,4,4,1,5,1,1,0,7,7,8,7,4,5,6]
print lis,'\n'

l = len(lis)

dic = {}
for i in lis:
        count = 0
       
        for j in lis:
                #print lis[c]
                if j == i:
                        count = count + 1
      
        #print i,'got it','count = ',count
        #print i
        dic[i]=count
#print dic
for key in dic:
        print 'element :', key, 'count repeat', dic[key]

```

 <pre>
  OUTPUT :
  </pre>
<pre>  
  [0, 3, 4, 3, 5, 4, 4, 1, 5, 1, 1, 0, 7, 7, 8, 7, 4, 5, 6] 

element : 0 count repeat 2
element : 1 count repeat 3
element : 3 count repeat 2
element : 4 count repeat 4
element : 5 count repeat 3
element : 6 count repeat 1
element : 7 count repeat 3
element : 8 count repeat 1
</pre>
