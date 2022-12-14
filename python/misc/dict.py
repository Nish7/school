# dictionaries
# collection of  key-value pairs
# obj with type dict
# it is mutable

obj = {"a": 1, "f": 2}

# Operations

# len returns list of key-value pairs
len(obj)

obj.keys()

obj.values()

for k in obj:
    # k --> is the key
    print(k)


# pop delets the inputted arguments , key and returns the value of deleted key as well.
print(obj.pop("a"))
