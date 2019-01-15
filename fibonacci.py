n = int(input(" Enter a number "))
a,b = 0,1
print(a,b,end = " ")
while(a<n):
    c = a+b
    print(c , end = " ")
    a,b = b, c
