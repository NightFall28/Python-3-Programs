# convert integer to character

user_str = input("Enter amount from 65 to 122: ")
user_value = user_str.split(",")

for i in range(len(user_value)):
    user_value[i] = chr(int(user_value[i]))
result = ','.join(user_value)
print(result)
