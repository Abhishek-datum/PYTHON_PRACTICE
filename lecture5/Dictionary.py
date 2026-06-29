# An unordered, mutable, collection of key-value pair
# Define using{}
# my_dict={"name":"Alice","age":25}
# key features:
#key must be unique
# values can be any type
# supports dynamics updates
# d= {
#     1:10,
#     "name":"ws",
#     "age":10,
#     "courseName":["MERN","PYTHON","C"]
#     }
# print(d[1])
# print(d.get(1))
# print(d['age'])
# print(d.get("ages"))
# print(d['courseName'][1])
student={
    "STO1":["Ram","ram@gmail.com"],
    "STO2":["Ravi","ravi@gmail.com"],
    "STO3":["Hello","hello@gmail.com"],
}
# print(student["STO1"])
# for key in student.keys():
#     print(key)
# print(student.keys())
# for key in student.keys():
#     print(key,student[key])
# for v in student.values():
#     print(v)
# for v in student:
#     print(v)
# for key,value in student.items():
#     print(key,value)

d={
     "name":"pradeep",
     "coursName":"python",
     "email":"pradeep@wscubetech.com",
     "phone":24234234
}
# print(d.get("email","ws@gmail.com"))
# d['phone']=354356
# print(d)
# d.update({"name":"pradeep rai","email":"pra@ws.com"})
# print(d)
# d['duration']="45 Days"
# print(d)
# del d['email']
# print(d)
# print(d.pop('phone'))
# print(d)
# d.popitem()
# print(d)
# d.clear()
d.setdefault("duration","2 Months")
print(d)