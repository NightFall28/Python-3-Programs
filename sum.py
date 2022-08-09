# sum of all integers within a given range

def int_sum(num1,num2):
    sum = 0
    for i in range(num1,num2+1):
        sum += i
    return sum

print("Sum of Integers = ", int_sum(1,10))
