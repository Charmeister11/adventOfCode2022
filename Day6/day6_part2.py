def main():
    file = open("day6_input.txt", "r")
    line = file.readlines()[0]
    print(f"main answer: {solve(line)}")


def solve(line: str):
    marker = ''
    distinct = 14
    for i in range(len(line) - distinct + 1):
        for j in range(distinct):
            if line[i + j] not in marker:
                marker += line[i + j]
        if len(marker) == distinct:
            return marker, (i + distinct)
            print(f"marker: {marker} at position {i + distinct}")
            # break
        marker = ''

def run_tests():
    testCase1()
    testCase2()
    pass

#Test
def testCase1():
    print(f"test case 1: {solve('abcdefghijklmn')}")
def testCase2():
    print(f"test case 2: {solve('aaaabbdasdbabcdeglkmnopqrs')}")




    # for i in range(len(line) - 4):
    #     first = line[i]
    #     second = line[i+1]
    #     third = line[i+2]
    #     fourth = line[i+3]
    #
    #     if (first != second and first != third and first != fourth
    #             and second != third and second != fourth
    #             and third != fourth):
    #         print(i+3+1)
    #         break


if __name__ == "__main__":
    main()
    run_tests()