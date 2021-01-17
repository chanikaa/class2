# Example1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # output: ['apple', 'cherry']

# Example2
thislist = ["apple", "banana", "cherry"]
thislist.pop("1")
print(thislist)  # output: ['apple', 'cherry']

# Example3
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  # output: ['apple', 'bannana']

# Example4
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # output: ['banana', 'cherry']

# Example5
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # output:[]
