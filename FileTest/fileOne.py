def readwriteFile():
    # fo = open("/home/sfcc/PycharmProjects/pythonProject2/FileTest/show.txt", "r+")
    with open("./show.txt", 'r+') as fo:
        fo.write("321396933")
        #str_read = fo.read(6)
        #print("读出的文件为:", str_read)
        print("文件名", fo.name)
        print("文件模式", fo.mode)
        print("文件是否关闭", fo.closed)

    # print("末尾是否强制加空格", fo.softspace)


if __name__ == '__main__':
    readwriteFile()
