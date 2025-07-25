student = {
    "name" : "dev",
    "age": 20,
    "grade": "A"
}
print(student["name"])

student["city"] = "delhi"
for key, value in student.items():
    print(key,"->",value)