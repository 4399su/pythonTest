def wrapper1(func1):
    print('set func1')

    def improved_func1():
        print('call func1')
        func1()

    return improved_func1


def wrapper2(func2):
    print('set func2')

    def improved_func2():
        print('call func2')
        func2()

    return improved_func2


# 装饰器1将装饰器2和函数当做一个闭包
@wrapper1
@wrapper2
def origin_func():
    pass


# 先增强，后调用
# 封装先输出，调用后输出
if __name__ == '__main__':
    origin_func()
