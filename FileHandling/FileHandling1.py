f = open("C:\\Users\\Harsh\\FileHandling\\Divy.txt","w")
t=int(input())
f.write(str(t)+"\n")
while(t!=0):
    n = int(input())
    f.write(str(n)+"\n")
    t=t-1
f.close()
#read() = Read everything
#readline() = Read line by line
#readlines() = list of the line