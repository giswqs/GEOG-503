print("Please enter x and y coordinates separated by space (enter 'done' to quit):")
print("Example: 0.5 0.5")

while True:
    coordinate = raw_input("Enter:")
    if coordinate.lower() == "done":
        break
    try:
        xy = coordinate.split(" ")
        x = float(xy[0])
        y = float(xy[1])
        if 0 <= x <= 1 and 0 <= y <= 1:
            print('({0},{1}) is in the box.'.format(x, y))
        else:
            print('({0},{1}) is outside the box.'.format(x, y))
    except:
        print("invalid input")