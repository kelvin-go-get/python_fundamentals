#Built-in Library functions
y = max(56,57,58,59,60)
print(y)

x = min(50,51,52,53,54,55)
print("the minimum value is ",x)

z=pow(2,3)
print(z)

#user-defined functions
def greeting():
    print("Hello")
greeting()

def multiply(a,b):

    print(a*b)
multiply(2,3)

#parameters/variables and arguments/values
def add(a,b):
    print(a+b)
add(2,3)

def employee(fullname,age,position,status):
    print(fullname,age,position,status)
employee("Mark Joe",30,"CEO","Married")
