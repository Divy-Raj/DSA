f = open("C:\\Users\\Harsh\\FileHandling\\Divy.txt","r")
#print(f.read()) # If we have given argument 3 in read function then it read first 3 character
#print(f.readline()) # It will simply print first line
#for line in f:
#    print(line,end=" ")
#print(f.readlines())
#read() = Read everything
#readline() = Read line by line
#readlines() = list of the line
data = f.readlines()
print(data)
for line in data:
    word = line.split()
    print(word)