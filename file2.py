import pickle
import json
#1)
dict = [{"key1": "hello"},
        {"key2": "hello"},
        {"key3": "hello"},
        {"key4": "hello"}]
with open("../dict.txt", "wb") as f:
    pickle.dump(dict, f)
#2)
a = {"key": 1,
     "key2": True}
b = {"key": "Hello"}
c = {}
for key, value in a.items():
    if key in b:
        c[key] = [value, b[key]]
    else:
        c[key] = value
for key, value in b.items():
    if key not in c:
        c[key] = value
with open("../result.json", "w") as f:
    json.dump(c, f)