import json

d = {"a": 1}
l = [1, 2.2]
t = (3, 4)
s = 'Hello World'
b = True
none = None
st = {1, 2, 'Test'}

print(json.dumps(d))
print(json.dumps(l))
print(json.dumps(t))
print(json.dumps(s))
print(json.dumps(b))
print(json.dumps(none))
# print(json.dumps(st)) # TypeError: Object of type set is not JSON serializable

obj = {"dict": d, "list": l, "tuple": t, "str": s, 'bool': b, 'none': none}
with open('storage.json', 'w') as f:
    json.dump(obj, f)
