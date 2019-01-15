n = int(input(" Enter the Number "))
mod = 0
while(n>0):
    m = n%10
    n = n//10
    mod = mod+m
print ( "Sum of Digit", mod)
