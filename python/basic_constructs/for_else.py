def try_for_else_usual():
    run_list = [1, 2]
    for item in run_list:
        print(item)
    else:
        print('\tfor loop else')
    print(' end of for loop else')


def try_for_else_empty():
    run_list = []
    for item in run_list:
        print(item)
    else:
        print('\tfor loop else empty')
    print(' end of for loop else empty')


def try_for_else_break():
    run_list = [1]
    for _ in run_list:
        break
    else:
        print('\tfor loop else with break')
    print(' end of for loop else with break')


def try_for_else_raise():
    run_list = [1]
    try:
        for _ in run_list:
            raise Exception('raised from inside for loop')
        else:
            print('\tfor loop else with raise')
    except Exception as e:
        pass
    print(' end of for loop else with raise')


if __name__ == '__main__':
    try_for_else_usual()
    try_for_else_empty()
    try_for_else_break()
    try_for_else_raise()
