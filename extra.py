#printing board for 3x3 grid
def print_3x3(Board):
    for i in range(len(Board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(Board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(Board[i][j])
            else:
                print(str(Board[i][j]) + " ", end="")

#printing board for 4x4 grid
def print_4x4(Board):
    for i in range(len(Board)):
        if i % 4 == 0 and i != 0:
           print("----------------------------------------")
        for j in range(len(Board[0])):
            if j % 4 == 0 and j != 0:
                print(" | ", end="")
            if j == 15:
                print(Board[i][j])
            else:
                print(Board[i][j], "", end="")