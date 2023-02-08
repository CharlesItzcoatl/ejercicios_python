def read():
    numbers = []
    with open("/home/charles/Documents/curso_python/archivos/numbers.txt", "r", encoding="utf-8") as f:
    #with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
        print (numbers)


def write():
    names = ["Peludi"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for element in names:
            f.write(element)
            f.write("\n")


def run():
    read()


if __name__ == '__main__':
    run()