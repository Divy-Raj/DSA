# Find Last and First Digit of given Number
# Find First Digit of any number
# 1st Method
n = int(input())
rem = 0
while(n>0):
    rem = n%10
    n = n//10
print(rem)
# 2nd Method
t = input()
print(t[0])
# Find Last Digit of any number
# 1st Method
p = int(input())
Last = p%10
print(Last)
