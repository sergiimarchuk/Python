

```python
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello() ## returns "<b><i>hello world</i></b>"
```

<pre> http://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators-in-python/739665#739665 </pre>

```Python
#!/usr/bin/python
import psutil

def mydecorator(func):
        def wrapper1():
                #print "a" + func()
                return "Checking MEMORY USGAE: " + func()
        return wrapper1

#@mydecorator
#def hello():
#   return "hello world"


@mydecorator
def memory_usage_status():
            """ Check Usage memory """
            percentUsed = psutil.virtual_memory().percent
            virt = psutil.virtual_memory()

            total_threshold1= int(virt.total / 1024 / 1024)

            if percentUsed > 80 and percentUsed < 90:
                print "Memory usage. Status Warning. " + str(percentUsed) + "%"
            if percentUsed >= 90:
                return "Memory usage. Status Crtitical. " + str(percentUsed) + "%"
            if percentUsed < 80:
                return "Memory usage. Status OK. " + str(percentUsed) + "%"

s_u = memory_usage_status()
print s_u


#print hello()
```


```Python

#!/usr/bin/python
import psutil

def mydecorator(func):
    def wrapper1():
        #print "a" + func()
        return "Checking MEMORY USGAE: " + func()
    return wrapper1

#@mydecorator
#def hello():
#   return "hello world"

def collect_into_list(func):
    collect_list = []
    def wrapper2():
        collect_list.append(func())
        return collect_list
    return wrapper2


@collect_into_list
@mydecorator
def memory_usage_status():
    """ Check Usage memory """
    percentUsed = psutil.virtual_memory().percent
    virt = psutil.virtual_memory()

    total_threshold1= int(virt.total / 1024 / 1024)

    if percentUsed > 80 and percentUsed < 90:
        return "Memory usage. Status Warning. " + str(percentUsed) + "%"
    if percentUsed >= 90:
        return "Memory usage. Status Crtitical. " + str(percentUsed) + "%"
    if percentUsed < 80:
        return "Memory usage. Status OK. " + str(percentUsed) + "%"

s_u = memory_usage_status()
print s_u


#print hello()

<pre>
We have to get this output
['Checking MEMORY USGAE: Memory usage. Status OK. 71.2%']
</pre>
