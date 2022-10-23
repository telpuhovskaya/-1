def isPalindrome(number):
    temp=number
    res = 0
    while(number>0):
        digit=number%10
        res=res*10+digit
        number=number//10
    if(temp==res):
        return True
    else:
        return False