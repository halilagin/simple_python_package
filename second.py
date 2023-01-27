
"""
write me for loop that run over  the list below

a=[
    {"share_name":"TESLA", "minute":0,"price":124},
    {"share_name":"TESLA", "minute":1,"price":124.2},
    {"share_name":"TESLA", "minute":2,"price":124.1},
    {"share_name":"TESLA", "minute":3,"price":124.5},
]
"""


data_string="""
[
    {"share_name":"TESLA", "minute":0,"price":124},
    {"share_name":"TESLA", "minute":1,"price":124.2},
    {"share_name":"TESLA", "minute":2,"price":124.1},
    {"share_name":"TESLA", "minute":3,"price":124.5}
]
"""


import json

print(" Tesla Price Changes")
data = json.loads(data_string) #json.load(filepath)
for item in data:
    print(f"Minutes {item['minute']} Price {item['price']}")



data_string = json.dumps(data)

f=open("./data.json", "w")
f.write(data_string)
f.close()




f=open("./data.json", "r")
lines = f.read()

print("file content")
print(lines)




