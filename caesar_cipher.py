# encrypt and decrypt a file

def encrypt(user_file,s):
    my_file = open(user_file, 'r+')
    L = my_file.read()
    L = list(L)
    UTF_upper = [chr(i) for i in range(65,91)]
    UTF_lower = [chr(i) for i in range(97,123)]
    num_set = ['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(L)):
        if(L[i] >= 'A' and L[i] <= 'Z'):
            k = 1
            index = UTF_upper.index(L[i])
            while(k <= s):
                L[i] = UTF_upper[(index+1)%26]
                k += 1

        elif(L[i] >= 'a' and L[i] <= 'z'):
            k = 1
            index = UTF_lower.index(L[i])
            while(k <= s):
                L[i] = UTF_lower[(index-1)%26]
                k += 1

        elif(L[i] >= '0' and L[i] <= '9'):
            k = 1
            index = num_set.index(L[i])
            while(k <= s):
                L[i] = num_set[(index-1)%10]
                k += 1
    L = ''.join(L)
    my_file.seek(0)
    my_file.write(L)
    my_file.close()

def decrypt(user_file,s):
    my_file = open(user_file, 'r+')
    L = my_file.read()
    L = list(L)
    UTF_upper = [chr(i) for i in range(65, 91)]
    UTF_lower = [chr(i) for i in range(97, 123)]
    num_set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(L)):
        if (L[i] >= 'A' and L[i] <= 'Z'):
            k = 0
            index = UTF_upper.index(L[i])
            while (k < s):
                L[i] = UTF_upper[(index - 1) % 26]
                k += 1

        elif (L[i] >= 'a' and L[i] <= 'z'):
            k = 0
            index = UTF_lower.index(L[i])
            while (k < s):
                L[i] = UTF_lower[(index + 1) % 26]
                k += 1

        elif (L[i] >= '0' and L[i] <= '9'):
            k = 0
            index = num_set.index(L[i])
            while (k < s):
                L[i] = num_set[(index + 1) % 10]
                k += 1
    L = ''.join(L)
    my_file.seek(0)
    my_file.write(L)
    my_file.close()

user_file = input("Enter file name: ")
s = int(input("Enter s: "))
encrypt(user_file,s)
decrypt(user_file,s)
