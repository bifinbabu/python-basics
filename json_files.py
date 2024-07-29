import json

book = {}

book["tom"] = {"name": "tom", "address": "1 street NU", "phone": 5667}
book["bob"] = {"name": "bob", "address": "1 sdgfh NU", "phone": 5688}

print(book)

s = json.dumps(book)
with open("/Users/iriplb/Desktop/reference/python-basics/book.json", "w") as f:
    f.write(s)
with open("/Users/iriplb/Desktop/reference/python-basics/book.txt", "w") as f:
    f.write(s)
print(s)
