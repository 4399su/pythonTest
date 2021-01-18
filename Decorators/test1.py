import datetime


def print_odds():
    for i in range(100):
        if i % 2 == 1:
            print(i)


# 闭包函数参数和返回值都是函数
# 函数增强
def count_time_wrapper(func):
    def improved_func():
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        print("it takes{}s to find the odds".format(end_time - start_time))

    return improved_func


if __name__ == '__main__':
    print_odds = count_time_wrapper(print_odds)
    print_odds()
