# 通过装饰器进行函数增强，只是一种语法糖，本质上跟上个程序完全一致
# 装饰器本质上是函数闭包的一种语法糖
# 第一次调用时被增强，只增强一次，在调用第一次之前增强
import datetime


def count_time_wrapper(func):
    def improved_func():
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        print("it takes{}s to find the odds".format(end_time - start_time))

    return improved_func


@count_time_wrapper
def print_odds():
    for i in range(100):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    #print_odds = count_time_wrapper(print_odds)
    print_odds()
