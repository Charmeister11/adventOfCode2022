def main():
    input = open("day1_input.txt", "r")
    calories = []
    sum = 0
    for line in input:
        if line != "\n":
            sum += int(line)
        else:
            calories.append(sum)
            sum = 0
    calories.sort()
    print("Top gnelf: " + calories[-1])
    print("Top 3 gnelfs: " + calories[-1] + calories[-2] + calories[-3])
if __name__ == "__main__":
    main()


