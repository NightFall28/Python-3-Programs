# determine if 3 coordinate points form a triangle


def is_triangle():
    try:
        while(True):
            x1 = float(input("Enter x1: "))
            y1 = float(input("Enter y1: "))
            x2 = float(input("Enter x2: "))
            y2 = float(input("Enter y2: "))
            x3 = float(input("Enter x3: "))
            y3 = float(input("Enter y3: "))

            # shoelace formula for triangle area
            # The Heron's formula give me extremely small area when input is
            # (3,3), (5,5), and (6,6). But since I know these points are collinear, the area
            # need to be zero, so I look up shoelace formula instead.
            area = 0.5 * (x1 * (y2 - y3) + x2 * (y3-y1) + x3 * (y1-y2))
            if(area == 0):
                print("This is not a triangle")
            else:
                print("This is a triangle")
            user_decision = input("Continue? (Yes/No) ")
            if(user_decision == "No" or user_decision == "NO" or user_decision == "no"):
                return
    except(ValueError):
        print("Invalid Input, Please Try Again")
        is_triangle()

is_triangle()

