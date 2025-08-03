import os
from dotenv import load_dotenv
load_dotenv('Python_for_Git/Env and Json/test.env')
print("password:", os.getenv("password"))
import json
data = {
    "name": "Srav's",
    "age": 21,
    "skills": ["Python", "Trading", "Editing"]
}
with open("test1.json", "w") as f:
    json.dump(data, f, indent=2)
with open("test1.json", "r") as f:
    data = json.load(f)
print("Name:", data["name"])
print("skills:", ",".join(data["skills"]))
students = [
    {"name": "Raj", "marks": 90},
    {"name": "Simran", "marks": 85},
    {"name": "Aman", "marks": 78}
]
with open("students.json", "w") as f:
    json.dump(students, f, indent=2)
with open("students.json", "r") as f:
    students_data = json.load(f)
good_students = []
for student in students_data:
    if student["marks"] > 80:
        print(student["name"],"->", student["marks"])
        good_students.append(student["name"])
json_data=json.dumps(good_students, indent=2)
print("Good Students:", json_data)
json_str = '{"branch": "ECE", "rank": 512}'
data=json.loads(json_str)
print(data)



