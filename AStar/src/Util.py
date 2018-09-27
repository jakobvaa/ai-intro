def makeBoard(filename):
    file = open("../res/boards/" + filename, 'r')
    text = file.read()
    file.close()
    list = text.split("\n")
    list.pop()
    return list
