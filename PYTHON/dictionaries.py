#dictionaries
student ={
    "name":"YASWANTH",
    "age":21,
    "course":"MCA",
    "CGPA":8.8
}
student["city"]="kovvur"

print(student)
print(student["name"])
print(student.get("age"))
for key,value in student.items():
    print(key,"=",value)
