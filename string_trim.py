def string_trim(my_str, length_limit):
    # Pre-Condition from the question: any string A of length greater than k
    if(length_limit > len(my_str)):
        print("Invalid, the string length is smaller than the limit k")
    else:
        for i in range(len(my_str)):
            print(my_str[:len(my_str)-i])
            if(my_str[:len(my_str)-i] == my_str[:length_limit]):
                break

string_trim("Greetings", 3)
