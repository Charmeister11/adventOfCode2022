def main():
    file = open("day4_input.txt", "r")
    repeats = 0
    for line in file:
        line = line.replace("\n", "").split(",")
        elf1_min = int(line[0].split("-")[0])
        elf1_max = int(line[0].split("-")[1])
        elf2_min = int(line[1].split("-")[0])
        elf2_max = int(line[1].split("-")[1])

        if elf1_min <= elf2_min and elf1_max >= elf2_max:
            repeats += 1
        elif elf2_min <= elf1_min and elf2_max >= elf1_max:
            repeats += 1

    print(repeats)

if __name__ == "__main__":
    main()