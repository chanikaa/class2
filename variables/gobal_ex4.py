x = "awesome"


def myfunc():
    global x
    print("[-] Python is " + x)
    x = "fantastic"


myfunc()
print("Python is " + x)


# output : python is awesome
# output:[-] Python is fantastic