# https://www.youtube.com/watch?v=yiSdpYmZA2w


def enter_numbers_outer():
    numbers = []

    def enter_number(x):
        numbers.append(x)
        print(numbers)

    return enter_number


enter_number = enter_numbers_outer()
enter_number(3)
enter_number(7)
enter_number(4)


# [3]
# [3, 7]
# [3, 7, 4]