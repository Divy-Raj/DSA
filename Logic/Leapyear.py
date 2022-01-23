# 1 N % 4 == 0 : Required
# 2 N % 100 == 0 : May or may not be leap year
# 3 N % 400 == 0 : Leap year
def getLeapYear(year):
   if year % 4 == 0:
       if year % 100 == 0:
           if year % 400 == 0:
              print("Yes")
           else:
               print("No")
       else:
           print("Yes")
   else:
       print("No")

for _ in  range(int(input())):
    getLeapYear(int(input()))




