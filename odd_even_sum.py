# sum of all odd numbers and sum of all even numbers within a given range, starting from 0


def sum_of_odd_even():
    target = int(input("Enter the target number: "))
    odd_sum = 0
    even_sum = 0
    for i in range(0,target+1):
        if(i % 2 == 0):
            even_sum += i
        else:
            odd_sum += i
    print("Odd Sum = ",odd_sum,"\nEven Sum = ",even_sum)

sum_of_odd_even()
