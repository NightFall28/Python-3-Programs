# given the size of tables, randomly generates each value for the tables so that each table add up to 1

import random
size_n = int(input("Enter size of table: "))
table1 = [random.random() for i in range(size_n)]
table2 = [random.random() for i in range(size_n)]
sum1 = sum(table1)
sum2 = sum(table2)
table1 = [i/sum1 for i in table1]
table2 = [i/sum2 for i in table2]
print("Table 1:",table1)
print("Table 2:",table2)
