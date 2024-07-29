import json

f = open("/Users/iriplb/Desktop/reference/python-basics/book.txt", "r")
s = f.read()
print(s)

book = json.loads(s)
print(book)
print(type(book), type(s), book["bob"]["phone"])

for person in book:
    print(book[person])
