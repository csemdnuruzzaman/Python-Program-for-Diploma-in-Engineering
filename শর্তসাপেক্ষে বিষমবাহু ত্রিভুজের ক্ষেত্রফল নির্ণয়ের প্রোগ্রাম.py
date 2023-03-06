import math
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
if((a+b)>c) and ((b+c)>a) and ((c+a)>b):
    s =(a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the triangle is: ",area)
else:
    print("The triangle is not possible.")