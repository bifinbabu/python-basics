dic = {"hello": "world"}
print(dic["hello"])
dic["hi"] = "Bifin"
print(dic)

for key in dic:
    print("key:", key, "value:", dic[key])

for k, v in dic.items():
    print("key:", k, "value:", v)

print("hello" in dic)

del dic["hello"]
print(dic, dic["hi"])
