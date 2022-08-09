# Determine if a number is a perfect number

def perfect_number():
    try:
        while(True):
            num = int(input("Enter a number: "))
            if(num <= 0):  # excluding 0 and below (positive integer only)
                raise ValueError
            sum = 0
            for i in range(1,num):
                if(num % i == 0):
                    sum += i
            if(num == sum):
                print(num,"is a perfect number")
            else:
                print(num,"is NOT a perfect number")
            user_decision = input("Continue? (Yes/No) ")
            if (user_decision == "No" or user_decision == "NO" or user_decision == "no"):
                return
    except(ValueError):
        print("Invalid Input (Positive Integer Only), Try Again")
        perfect_number()   # Call function again when exception happens

perfect_number()
