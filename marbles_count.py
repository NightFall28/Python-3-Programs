# count how many marbles can fit into a sphere container


from math import pi
n = 70
radius = n/7
marble_volume = (4/3) * pi * (radius * radius * radius)
cube_volume = n * n * n
num_marbles = cube_volume // marble_volume
print(num_marbles, "marbles fit in the cube")

