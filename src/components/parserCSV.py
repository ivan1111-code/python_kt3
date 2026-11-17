def readFile(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def createSchema(csv, arrayGlobal, arrayCur, index, part):
    if index == len(csv):
        arrayCur.append(part)
        arrayGlobal.append(arrayCur)
        return arrayGlobal

    if csv[index] == "|":
        arrayCur.append(part)
        return createSchema(csv, arrayGlobal, arrayCur, index + 1, "")
    elif csv[index] == "\n":
        arrayCur.append(part)
        arrayGlobal.append(arrayCur)
        return createSchema(csv, arrayGlobal, [], index + 1, "")
    else:
        part += csv[index]
        return createSchema(csv, arrayGlobal, arrayCur, index + 1, part)


def substrFilter(books, curBookIndex, curWordIndex, curCharIndex, word, prefix):
    if curBookIndex == len(books) - 1: 
        return []
    if books[curBookIndex][-1] == books[curBookIndex][curWordIndex]:
        return substrFilter(books, curBookIndex + 1, 0, 0, "", prefix)
    if books[curBookIndex][curWordIndex][-1] == books[curBookIndex][curWordIndex][curCharIndex]:
        return substrFilter(books, curBookIndex, curWordIndex + 1, 0, "", prefix)
    if word == prefix:
        return books[curBookIndex]

    word += books[curBookIndex][curWordIndex][curCharIndex]

    return substrFilter(books, curBookIndex, curWordIndex, curCharIndex + 1, word, prefix)    


def booksCounter(books, curBook, array):
    if curBook == len(books) - 1:
        return array
    
    array.append((books[curBook][0], float(books[curBook][-1]) * int(books[curBook][-2])))
    return booksCounter(books, curBook + 1, array)