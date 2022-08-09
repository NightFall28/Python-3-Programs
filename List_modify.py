# modify the list so that each element is swapped with the largest element to the right of that element, last element become 0
# [5,3,2,3] --> [3,3,3,0]

class Answer:
    def swapItems(self, L):
        for i in range(len(L)):
            if(L[len(L)-1] == L[i]):
                L[i] = 0
                break
            max = L[i+1]
            j = i+1
            while(j < len(L)):
                if(L[j] > max):
                    max = L[j]
                j += 1
            L[i] = max
        return L

L = []
size = int(input("Enter the size of the list L: "))
for i in range(size):
    # Since the question did not specify the data type for the elements,
    # I used float type so that it works in most general cases.
    L.append(float(input("Enter a value: ")))

my_instance = Answer()
print("List Lm is:",my_instance.swapItems(L))
