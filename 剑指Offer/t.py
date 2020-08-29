import os



def genDirName():
    res = []
    for i in range(1, 101, 10):
        res.append("{0}~{1}".format(i, i+9))
    return res


def create():
    names = genDirName()
    for name in names:
        if not os.path.exists(name):
            os.mkdir(name)


if __name__ == '__main__':
    create()
