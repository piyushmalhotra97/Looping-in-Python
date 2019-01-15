a , b = 0 , 1
n = int(input(" Enter a Number" ))
print (a,b,end = " ")
for i in range(2,n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
