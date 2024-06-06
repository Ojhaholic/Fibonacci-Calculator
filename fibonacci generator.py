#The python program will give you first n fibonacci numbers in an array (list)

print("Fibonacci Calculator")
print()

#Specifying how many numbers you want in series

n= int(input("Number of items = "))

#printing 0 or 0&1 if the series is max of 2 items

if n==1:
    print([0])
elif n==2:
    print([0,1])

#expanding the series
    
else:
    a=0
    b=1
    l=[]
    for i in range(0,n):
        c=a+b
        a=b
        b=c
        l.append(c)
    print(l)
        
