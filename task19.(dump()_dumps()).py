# Difference Between Dump() function and Dumps() function.
# 1. json.dumps() - This method allows you to convert a python object into a serialized JSON object.
# 2. json.dump() - This json.dump() method can be used for writing to JSON file.

# Difference Between Load() function and Loads() function.
# 1. json.loads() - Deserializes a JSON object to a standard python object.
# 2. json.load() - Deserializes a JSON file object into a standard python object.

def my_func(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s : %s" % (key, value))
my_func("DAVIET", Name = "YUVRAJ", Place = "Jalandhar")