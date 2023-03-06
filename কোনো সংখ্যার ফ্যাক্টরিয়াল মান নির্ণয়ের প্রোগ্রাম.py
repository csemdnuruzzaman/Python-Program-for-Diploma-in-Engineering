fact = int(input("Enter a number: "))
sum = 1
result = 1
if(fact ==0):
    print("The factorial is=",1)
elif(fact<0):
    print("Sorry, Factorial does not exist for negative numbers")
else:
    while(sum<=fact):
        result = result*sum
        sum = sum+1
    print("The factorial is=",result)