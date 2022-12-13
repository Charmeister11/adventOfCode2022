def main():
    file = open("day6_input.txt", "r")
    line = file.readlines()[0]
    for i in range(len(line) - 4):
        first = line[i]
        second = line[i+1]
        third = line[i+2]
        fourth = line[i+3]

        if (first != second and first != third and first != fourth
                and second != third and second != fourth
                and third != fourth):
            print(i+3+1)
            break


if __name__ == "__main__":
    main()