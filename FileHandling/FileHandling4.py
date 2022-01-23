f = open("C:\\Users\\Harsh\\FileHandling\\Divy.txt","w")
r = open("C:\\Users\\Harsh\\FileHandling\\Divy2.txt","r")
t = int(r.readline())
while(t>0):
    n = int(r.readline())
    data = r.readline()
    arr = list(map(int,data.split()))
    min = arr[0]
    ind = None
    for i in range(1,n):
        if(arr[i]<min):
            min = arr[i]
            ind = i

    f.write(str(ind)+"\n")
    t=t-1