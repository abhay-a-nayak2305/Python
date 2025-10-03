def factorial(a):
    if a<2:
        return 1
    else:
        return a*factorial(a-1)

fact=factorial(5)
print("The factorial of 5 is: ",fact)