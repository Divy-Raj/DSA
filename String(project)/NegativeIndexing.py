#Negative Indexing
st = "Prep Bytes"
print(st[0])
print(st[-10])
print(st[1])
print(st[-9])

#Slicing
print(st[0:6])
print(st[2:7])
print(st[:7])
print(st[:])
print(st[5:] + st[:4])
print(st[-6:2]) #Nothing is printed here because starting is before then ending but index is positive and negative
print(st[-6:-2])
print(st[-6:8])
print(st[-6:7])
print(st[-6:3])

#Slicing with steps and join method
#slicing with steps
print(st[0:7:3])
print(st[:8:2])
print(st[0::5])
print(st[::-1])
print(st[6:8:-1])

#if we want to change any string indexing then it cannot happen i.e
#st[7]= "z" #it will simply print error
#But you can change this by using list
st = list(st)
st[7] = "z"
print(st)
#so it is change at given index.you can write same thing in string by using str() method
print(str(st))
#but if you want this thing in revers order
#or you can say change list character into given character
#Here we use join method
st1 = "1"
print(st1.join(st))
#so at the given example above at every space character 1 will come
# or you can write this method in other method
st1 = "".join(map(str,st))
print(st1)
