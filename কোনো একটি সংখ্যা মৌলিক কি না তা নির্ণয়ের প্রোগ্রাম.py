i=2
n = int(input("Enter the number to check prime: "))
while(i<n):
    r = n%i
    i = i+1
    if(r==0):
        break
if(r==0):
    print(n,"is not a prime number.")
else:
    print(n,"is a prime number.")