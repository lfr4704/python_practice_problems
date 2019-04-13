import json

with open('phone.json') as f:
    my_var = json.load(f)
    print(my_var)
