# sum of each digit.
# ex.  123 = 1 + 2 + 3 = 6

user_number = int(input("Enter a number: "))
sum = 0
while(user_number != 0):
    sum += user_number % 10
    print(user_number % 10)
    user_number = user_number // 10
print("The sum of all digits is: ",sum)
