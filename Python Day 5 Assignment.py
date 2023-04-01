x=int(input("Enter the number:"))
if(x%3==0)and(x%5==0):
    print("FIZZBUZZ")
elif (x%3==0):
    print("FIZZ")
elif(x%5==0):
    print("BUZZ")
else:
    print("Not Divisible by both")
