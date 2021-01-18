import os


def readwriteFile():
    # fo = open("/home/sfcc/PycharmProjects/pythonProject2/FileTest/show.txt", "r+")
    with open("./realShow.txt", 'r+') as fo:
        fo.write("321396933")
        fo.flush()
        str_read = fo.read()
        print("读出的文件为:", str_read)
        print("文件名", fo.name)
        print("文件模式", fo.mode)
        print("文件是否关闭", fo.closed)
        position = fo.tell()
        print("文件的当前位置：", position)

        # 参数1-当前文件名  参数2-修改后文件名
        # os.rename("./show.txt", "./realShow.txt")

        # 新建文件夹
        #os.mkdir("./new_Directory")

        # 更改当前工作文件夹，一个参数，为新文件夹
        #os.chdir("file")

        # 删除文件夹
        os.rmdir("./new_Directory")

        # 删除文件
        # os.remove("./realShow.txt")

        # 参数1 偏移量  参数2 文件指针移动位置 0为开始 1为当前 2为末尾
        fo.seek(0, 0)

    # print("末尾是否强制加空格", fo.softspace)


if __name__ == '__main__':
    readwriteFile()
