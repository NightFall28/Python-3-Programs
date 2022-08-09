# copy odd or even lines from one file to another file.

with open("random.txt","r") as f1:
    user_decision = input("Odd/Even? ")
    if(user_decision == "Even" or user_decision == "even"):
        f2 = open("random2.txt","w")
        f2_list = []
        f1_list = f1.readlines()
        for i in range(len(f1_list)):
            if(i % 2 != 0):
                f2_list += f1_list[i]
        f2.writelines(f2_list)
        f2.flush()
        f2.close()
    elif(user_decision == "Odd" or user_decision == "odd"):
        f2 = open("random2.txt", "w")
        f2_list = []
        f1_list = f1.readlines()
        for i in range(len(f1_list)):
            if (i % 2 == 0):
                f2_list += f1_list[i]
        f2.writelines(f2_list)
        f2.flush()
        f2.close()
    else:
        print("Invalid Input")
