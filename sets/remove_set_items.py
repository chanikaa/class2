# Ex1
thisset = {"apple", "bannana", "cherry"}
thisset.remove("banana")
print(thisset)  # output: {'cherry', 'apple',  'orange'}

# Ex2
thisset = {"apple", "bannana", "cherry"}
thisset.discard("banana")
print(thisset)  # output: {'cherry', 'apple'}

# Ex3
thisset = {"apple", "bannana", "cherry"}
x = thisset.pop()
print(thisset)  # output: {'cherry', 'banana'}

# Ex4
thisset = {"apple", "bannana", "cherry"}
thisset.clear()
print(thisset)  # output: set()
