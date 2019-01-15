n = int(input(" Enter the Number "))
mod = 0
p = n
while(n>0):
    m = n%10
    n = n//10
    mod = mod*10+m
print(" Sum of digit :",mod)
if p==mod:
    print(" Number is palindrome ")
else:
    print(" Number is not palindrome ")
