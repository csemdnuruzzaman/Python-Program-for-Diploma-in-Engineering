n = int(input("Enter a number: "))
if(n<0):
    print("Please Enter positive number.")
else:
    sum = 0
    for i in range(1, n + 1, 1):
        sum = sum + i
    print("The sum is=",sum)

