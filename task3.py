def reverseNumber(number):
    isLessThanZero = False
    if number < 0:
        isLessThanZero = True
    result = 0
    number = abs(number)
    while number  > 0:
        digit = number % 10
        number = number // 10
        result = result * 10
        result = result + digit 
    if(isLessThanZero):
        result = result * -1
    return result