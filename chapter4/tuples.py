a=(1,2,3,4)
print(type(a))
b=(1)
print(type(b)) #in rhis case python thonk that we are thinking about integer
c=(1,)
print(type(c)) #in this case python think we are talkig about the empty tuples and manage to get the exact output
d=(5,35.25,False,"aakash","rohan")
print(type(d))
print(a)
no=d.count(5)
print(no)

i=a.index(2)
print(i)
print(len(a))