#Note = When you give input to the console give it in small letter.If any of them is capital letter than error should be
t=int(input())
while(t>0):
    str = input()
    freq = [0]*26
    print()
    for i in range(len(str)):
        freq[ord(str[i])-97]+=1

    flag=0
    for i in range(0,26):
        if(freq[i]>1):
            print("{}={}".format(chr(i+97),freq[i]),end=" ")
            flag=1
    if(flag==0):
        print("-1")
    else:
        print("0")
t=t-1