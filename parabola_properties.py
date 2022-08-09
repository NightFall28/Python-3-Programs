# output vertex, directrix, and focus


def parabola_property(a,b,c):
    # Vertex:
    h = (-b/(2*a))
    k = ( (-1*(b*b - (4 * a * c))) / (4 * a) )
    # Directrix:
    y = k - (1 / (4*a))
    # Focus:
    focus_x = h
    focus_y = k + (1 / (4*a))
    print("Vertex: (",h,",",k,")")
    print("Directrix: ",y)
    print("Focus: (",focus_x,",",focus_y,")")

parabola_property(-1,8,-20)
