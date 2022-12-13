def main():
    file = open("day3_input.txt", "r")
    ans = 0
    for line in file:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        if line != first_half + second_half:
            print("something broke on line: " + line)
            break
        for i in first_half:
            if i in second_half:
                ans += chr_to_int(i)
                break
    print(ans)


def chr_to_int(x):
    if x.isupper():
        return ord(x) - 64 + 26
    else:
        return ord(x) - 96


if __name__ == "__main__":
    main()