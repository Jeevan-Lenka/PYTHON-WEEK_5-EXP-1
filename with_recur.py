def prime(n,i=2):
    if n<=1:
        return False
    if n==i:
        return True
    if n%i==0:
        return False
    return prime(n,i+1)
n=int(input("enter a number:"))
if prime(n):
    print("prime")
else:
    print("not prime")