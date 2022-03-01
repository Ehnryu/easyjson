# EasyJson
A way to use JSON efficiently and properly

### Installation:
`pip install easierjson`

### Usage:
```python
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
print("key hi: " + hi)
print("edit the data like normal")
d.data["bye"] = hi
print("write all the data currently done:")
d.write()
print("manually set data")
d.data = {}
d.write()
```


### Development:
Install buildproj:

`pip install buildproj`

`build --build`

In case of the binary not working:

`python buildbinary.py --build`

All processes are automated except for the sign in for pip, please be sure to also change the version and name in `setup.py`