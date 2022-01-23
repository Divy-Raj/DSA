#Note In python self is by default object
class student:
    def __init__(self,FN,LN,age):
        self.firstName = FN
        self.lastName = LN
        self.age = age

s1 = student("Divy","Raj","21")
s2 = student("shristi","srivastava","17")


print(s1.firstName,s1.lastName,s1.age)
print(s2.firstName,s2.lastName,s2.age)