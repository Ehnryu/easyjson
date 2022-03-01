import easyjson

print("get the dict")
d = easyjson.use("test.json")
print(d.data) # the raw data
print("or")
print(d.getraw())
print("edit the data:")
d.add("hi","bye") # add auto writes from whatever is done before
print("get the data:")
hi = d.get("hi")
print("edit the data like normal")
d.data["bye"] = hi
print("write all the data currently done:")
d.write()
d.data = {}
d.write()