student = {
    "101" : {"name" : "dev" , "marks" : "90"},
    "102" : {"name" : "aru" , "marks" : "95"}
}
for roll, info in student.items():
    print(f"roll no:{roll}")
    print("name:", info ["name"])
    print("marks:",info ["marks"])
