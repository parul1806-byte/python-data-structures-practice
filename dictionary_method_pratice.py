#1️⃣ Create a dictionary of student info
student ={'name':"parul",'age':22,'gender':"female"}
print(student)

#2️⃣ Add a new key city with value 'Delhi' to the dictionary.
student ={'name':"parul",'age':22,'gender':"female"}
student['city'] = 'delhi'
print(student)

 #4️⃣ Update the student’s age to 21
student ={'name':"parul",'age':22,'gender':"female"}
student.update({'age':21})
print(student)

#5️⃣ Print all keys and values using a loop
num = {'1':'one','2':'two','3':'three'}
for key in num:
    print(key, num[key])

#6️⃣ Count how many times the word "Python" appears in the dictionary values
text = {'subject':'python','year':'3','book':'python'}
count = 0
for v in text.values():# provide the values of the dict
    if v.lower()  == "python":# .lower to remove case sensitivity
        count+= 1
print("no times python appear in the value",count)

#7️⃣ Delete the key 'course' using pop()
content = {'course':'btech','year':'2026','colleage':'hrit'}
content.pop('course')
print(content)

#8️⃣ Clear the entire dictionary
content = {'course':'btech','year':'2026','colleage':'hrit'}
content.clear()
print(content)

#9️⃣Create a dictionary from a list of keys using fromkeys()
#🔟Remove the last inserted item using popitem()
content = {'course':'btech','year':'2026','colleage':'hrit'}
content['name'] = 'parul'
print(content)
content.popitem()# removes last inserted item.
print(content)

#11️⃣ Check if a key exists in the dictionary or not
person = {'name':'parul','age':'21','course':'btech'}
if 'age' in person.keys():
    print("yes")
else:
    print("no")

#12️⃣ Merge two dictionaries into one
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)

#13️⃣ Print only keys which have string values
data = {'name': 'Parul', 'age': 22, 'city': 'Delhi', 'score': 95}
for key in data:
    if str(data[key]).isalpha():
        print(key)

#14️⃣ Find the key with the maximum value
marks = {'Math': 80, 'English': 90, 'Science': 85}
max_value = max(marks.values())
for key in marks:
    if max_value == marks[key]:
        print(key)

#15️⃣ Find common keys between two dictionaries
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 4, 'c': 5, 'd': 6}
for key in d1:
    if key in d2:
        print(key)

#16️⃣: Remove a key only if it exists
marks = {'Math': 80, 'English': 90, 'Science': 85}
marks.pop('hindi',None)

#17️⃣:Convert two lists into a dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]



