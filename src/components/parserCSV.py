def readFile(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def createSchema(csv):
    curArr = []
    listArr = []
    curWord = ""

    for ch in csv:
        if ch == "|":
            curArr.append(curWord)
            curWord = ""
        elif ch == "\n":
            if curWord:
                curArr.append(curWord)
                curWord = ""
            listArr.append(curArr)
            curArr = []
        else:
            curWord += ch

    if curWord or curArr:
        if curWord:
            curArr.append(curWord)
        if curArr:
            listArr.append(curArr)

    return listArr


def substrFilter(books, prefix):
    result = []
    for book in range(1, len(books)):
        prefixIndex = 0
        isWord = False
        for ch in books[book][1]:
            if ch == prefix[prefixIndex]:
                if prefixIndex == len(prefix) - 1:
                    isWord = True
                    break
                prefixIndex += 1
            else:
                prefixIndex = 0

        if isWord is True:
            newArr = [ 
                books[book][0], 
                books[book][1] + ", " + books[book][2],
                books[book][3],
                books[book][4]
            ]
            result.append(newArr)
    return result


def booksCounter(books):
    result = []
    for book in range(len(books)):
        result.append((books[book][0], int(books[book][3]) * float(books[book][4])))
    return result