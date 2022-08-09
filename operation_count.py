#string1 = greece and string2 = fleece
#we change two characters, so the output is 2

#string1 = friday and string2 = fries
#output is 3


def operation_count(str1,str2):
    a = str1
    b = str2
    count = 0
    startIndex = 0
    endIndex = 0
    if(len(a) == len(b)):
        for i in range(len(a)):
            if(a[i] not in b):
                count += 1
        return count


    elif (len(a) > len(b)):

        for i in range(len(b)):
            j = a.find(b[i], startIndex)
            if (j >= 0):
                if (j - startIndex >= 1):
                    count += (j - startIndex)
                startIndex = j + 1
                endIndex = j
            elif (j == -1):
                startIndex += 1
                endIndex += 1
                count += 1
            if (i == len(b) - 1 and endIndex != len(a)):
                count += len(a) - 1 - endIndex
        return count

str1 = 'friday'
str2 = 'fries'
print("Operation Count:",operation_count(str1,str2))
