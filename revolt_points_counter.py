score = {1: 10, 2: 8, 3: 7, 4: 6, 5: 5, 6: 4, 7: 3, 8: 2, 9: 1, 10: 0, 11: 0}
classification = input()
blue = 0
green = 0

for index, value in enumerate(classification):
    if value == 'b' or value == 'B':
        blue += score[index + 1]
    elif value == 'g' or value == 'G':
        green += score[index + 1]
    else:
        print("Wrong letter!")

print("BLU", blue, " - GRN", green)