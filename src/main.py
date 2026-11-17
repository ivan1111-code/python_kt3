from components.parserCSV import *
from pprint import pprint

def start():
    csvContent = readFile("./utils/books.csv")
    schema = createSchema(csvContent, [], [], 0, "")
    fltr = substrFilter(schema, 0, 0, 0, "", "XSL")
    res = booksCounter(schema, 1, [])
    pprint(res)
if __name__ == "__main__":
    start()