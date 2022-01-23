#In python all the thing is class i.e int is also a class  but in c/c++/Java int is data type
#i.e is shown below
var = 9
print(var.bit_length())
# So as per output var is data type but it is treated as class in python.you cna see output which give binary length of 9
# Imperative - A series of instruction
#class Mobile:
#    def __init__(self):
#
#self.brandName = "Samsung"
#        self.color = "Black"
#        self.isJack = False

#    def calling(self):
#        print("Calling")
#      def cameraClick(self):
#        print("Picture is clicked")

#    def message(self):
#        print("Message Sent")




#def main():
#    m1 = Mobile()
#    print(m1.brandName)
#    print(m1.color)
#    print(m1.isJack)
#    m1.calling()
#    m1.cameraClick()
#    m1.message()
#    print("---------------------------------------------")
#    m2 = Mobile()
#    print(m2.color)
#    print(m2.brandName)
#    print(m2.isJack)



#if __name__ == '__main__':
#    main()


# This mobile m1 and m2 have same color if i want m1 and m2 have different brand name, colour ,  etc. properties
# So we have to pass the argument init function
# and in place of object we write brand name , color etc.
class Mobile:
    def __init__(self,brandName,color,isJack):
        self.brandName = brandName
        self.color = color
        self.isJack = isJack

    def calling(self):
        print("Calling")
    def cameraClick(self):
        print("Picture is clicked")

    def message(self):
        print("Message Sent")





def main():
    m1 = Mobile("Apple","White",False)
    print(m1.brandName)
    print(m1.color)
    print(m1.isJack)
    m1.calling()
    m1.cameraClick()
    m1.message()
    print("---------------------------------------------")
    m2 = Mobile("OnePlus","Blue",True)
    print(m2.color)
    print(m2.brandName)
    print(m2.isJack)



if __name__ == '__main__':
    main()

#Please compare the both code as given above