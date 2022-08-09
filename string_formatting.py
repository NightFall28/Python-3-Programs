# given the input format: lastname, id, GPA, firstname
# output: id firstname lastname

Str = "Random,1234,3.99,Soul"
holder = Str.split(',')
StrOutput = holder[1] + " " + holder[3] + " " + holder[0]
print(StrOutput)
