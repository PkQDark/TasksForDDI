import time


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time()-t))
        return res

    return tmp


class NumOfCases(Exception):
    pass


class NumOfLines(Exception):
    pass


def len_of_file(file):
    return sum(1 for l in open(file, 'r'))


def num_of_cases(name_of_input):
    with open(name_of_input) as phone_input:
        num_of_case = int(phone_input.readline())
        num_of_lines = len_of_file(name_of_input)
        try:
            if not (0 < num_of_case <= 40):
                raise NumOfCases(Exception)
            if not (0 < num_of_lines <= 40000):
                raise NumOfLines(Exception)
        except Exception:
            return
        return num_of_case


def is_consistent(list_of_lists):
    for list in list_of_lists:
        for i in range(len(list)):
            temp = list[0]
            for k in range(len(list) - 1):
                if list[k+1].startswith(temp):
                    return True
            list.remove(list[0])
    return False


@timer
def check(name_of_input):
    t = num_of_cases(name_of_input)
    if t:
        with open(name_of_input) as phone_input:
            phone_input.readline()

            for i in range(t):
                count = int(phone_input.readline())
                numbers_of_one_case = []
                for j in range(count):
                    numbers_of_one_case.append(phone_input.readline()[:-1])
                separated_for_num_case = []
                list_of_separated_lists = []
                for i in range(10):
                    temp_for_num_separate = []
                    for j in numbers_of_one_case:
                        if j[:1] == str(i):
                            temp_for_num_separate.append(j)
                    if temp_for_num_separate:
                        separated_for_num_case.append(temp_for_num_separate)
                for i in separated_for_num_case:
                    temp_for_sort_separated = []
                    for k in sorted(i, key=lambda x: len(x)):
                        temp_for_sort_separated.append(k)
                    list_of_separated_lists.append(temp_for_sort_separated)

                #t = time.time()
                ch = is_consistent(list_of_separated_lists)
                #print("время расчетов")
                #print(time.time() -t)
                with open('phone.out', 'a') as out:
                    if ch:
                        out.write('No\n')
                    else:
                        out.write('Yes\n')
        print('alright!!')
    else:
        print('Wrong num of case or num of lines')

if __name__ == '__main__':
    check('test.in')