# Dictionary + function demo
def greet(user):
    return "Hello " + user["name"]

person = {"name": "Sravan", "age": 21}
print(greet(person))
