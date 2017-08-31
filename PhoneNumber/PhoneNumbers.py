def is_consistent(l):
    for i in range(len(l) - 1):
        if l[i + 1].startswith(l[i]):
            return True
    return False


def check():
    t = int(input())
    for _ in range(int(t)):
        count = int(input())
        numbers_of_one_case = []
        for j in range(count):
            numbers_of_one_case.append(str(input()))
        numbers_of_one_case = sorted(numbers_of_one_case)
        if is_consistent(numbers_of_one_case):
            print('NO')
        else:
            print('YES')


check()
