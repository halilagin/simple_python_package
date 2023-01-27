
"""
js:

let students = [
{"name":"halil", "surname":"agin", "age": 43},
{"name":"abc", "surname":"xyz", "age": 23}

]

function fun1() {
    for s in students {
        console.log(s.name)

    }
}

"""


class Student():
    #name,surname, age

    def __init__(self, obj):
        self.name = obj["name"]
        self.surname = obj["surname"]
        self.age = obj["age"]



students = [
    {"name":"halil", "surname":"agin", "age": 43}, #dictionary -> json objects
    {"name":"abc", "surname":"xyz", "age": 23}
]

def fun1():
    for s in students:
        s=Student(s)
        print (s.name)



fun1()