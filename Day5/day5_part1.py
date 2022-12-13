def main():
    file = open("day5_input.txt", "r")
    start = [["EMPTY"],
             ["H","R","B","D","Z","F","L","S"],
             ['T','B','M','Z','R'],
             ['Z','L','C','H','N','S'],
             ['S','C','F','J'],
             ['P','G','H','W','R','Z','B'],
             ['V','J','Z','G','D','N','M','T'],
             ['G','L','N','W','F','S','P','Q'],
             ['M','Z','R'],
             ['M','C','L','G','V','R','T']]

    all_lines = file.readlines()
    for line_nr in range(10, len(all_lines)):
        temp = all_lines[line_nr].split(" ")
        move = [int(temp[1]), int(temp[3]), int(temp[5])]
        for i in range(move[0]):
            start[move[2]].append(start[move[1]].pop())
    for i in range(1, len(start)):
        print(start[i][-1], end='')


if __name__ == "__main__":
    main()

  # inp = input()
    # while inp != "end":
    #     for i in inp:
    #         print("'" + i + "'" + ",", end="")
    #     inp = input()