'''
Test
Size
Element of Array space generated
'''
import random
f = open("C:\\Users\\Harsh\\FileHandling\\Divy.txt","w")
t=10
f.write(str(t)+"\n")
for i in range(t):
    size = random.randrange(1,10)
    f.write(str(size)+"\n")
    for j in range(size):
        ele = random.randrange(0,10)
        f.write(str(ele)+" ")
    f.write("\n")