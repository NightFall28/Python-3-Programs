# list all prime numbers within a given range


def find_prime():
    try:
        num1 = int(input("Enter lower bound: "))
        num2 = int(input("Enter upper bound: "))
        if(num1 < 0 or num2 < 0):
            raise ValueError
        for i in range(num1+1,num2):
            if i > 1:
                is_prime = True
                for j in range(2,i):
                    if(i % j == 0):
                        is_prime = False
                        break
                if(is_prime):
                    print(i,"is a prime number")
    except(ValueError):
        print("Invalid Boundary")

find_prime()
