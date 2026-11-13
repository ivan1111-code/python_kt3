from components.parserCSV import *
from pprint import pprint

def start():
    csvContent = readFile("./utils/books.csv")
    schema = createSchema(csvContent)
    result = substrFilter(schema, "XSLT")
    result2 = booksCounter(result)
    pprint(result2)
if __name__ == "__main__":
    start()