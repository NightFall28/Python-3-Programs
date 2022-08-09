# This program will check if any 3 values in the tuple will satisify the pythagorean theorem.

def pythagorean(tuple1,size):
    if(size < 3):
        return False
    for i in range(0,size-2):
        for j in range(1,size-1):
            for k in range(2,size):
                x = tuple1[i]
                y = tuple1[j]
                z = tuple1[k]
                if(x**2 == y**2 + z**2 or y**2 == z**2 + x **2 or z**2 == x**2 + y**2):
                    return True
    return False

size = int(input("Enter size of tuple: "))
list1 = []
for i in range(size):
    list1.append(float(input("Enter a value for tuple: ")))
tuple1 = tuple(list1)
print("Tuple:",tuple1)

print(pythagorean(tuple1,size))
