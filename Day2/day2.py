def main():
    loss = 0
    draw = 3
    win = 6
    switch = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    my_score = 0
    file = open("day2_input.txt", "r")
    for line in file:
        enemy = line[0]
        me = line[2]

        if enemy == "A":
            if me == "X": #need to lose
                my_score += (loss + 3)
            elif me == "Y": #need to draw
                my_score += (draw + 1)
            elif me == "Z": #need to win
                my_score += (win + 2)

        elif enemy == "B":
            if me == "X":
                my_score += (loss + 1)
            elif me == "Y":
                my_score += (draw + 2)
            elif me == "Z":
                my_score += (win + 3)

        elif enemy == "C":
            if me == "X":
                my_score += (loss + 2)
            elif me == "Y":
                my_score += (draw + 3)
            elif me == "Z":
                my_score += (win + 1)

        # my_score += switch.get(me)
    print(my_score)

if __name__ == "__main__":
    main()