def countdown(num):
    print(f"counting down from {num}")
    n = num
    while n > 0:
        yield n
        n -= 1
    print(f'Done count down from {num}')


def juggle_countdown():
    for num in countdown(5):
        print(num)


if __name__ == '__main__':
    juggle_countdown()