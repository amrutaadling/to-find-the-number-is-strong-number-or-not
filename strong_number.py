def factorial(n):
    if n==0 or n==1:
        return 1
    
    else :
        return n*factorial(n-1)
    
def strong_number (num):
    orignal_num=num
    sum=0

    if num==0:
        sum += factorial(num)
    
    while num>0:
        digit=num%10
        sum += factorial(digit)
        num //= 10

    if orignal_num==sum:
        return orignal_num
    
    else :
        return None


print(strong_number(123))