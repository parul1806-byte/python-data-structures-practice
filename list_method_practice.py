
#1. Create a list of 5 cities. Print the second city,
# add a new city at the end, insert one at index 2,
# and remove one city from the list.
from multiprocessing.reduction import duplicate

cities = ['delhi','indore','shamli','allhabaad']
print(cities[1])
cities.append('noida')# add item at the last
print(cities)
cities.insert(2,'baghpat')
print(cities)
cities.pop(2)
print(cities)

#2. Given a list: marks = [87, 45, 92, 67, 89],
# sort the marks, remove the lowest mark, and add 100 at the end.
marks = [87, 45, 92, 67, 89]
marks.sort()
print("sorted marks are :",marks)
marks.pop(0)
print(" after lowest mark has been removed",marks)
marks.append(100)
print("new list of marks is:",marks)

#3.. Given a list: names = ["Riya", "Parul", "Aman", "Parul", "Sahil"],
# count how many times "Parul" appears,

names = ["Riya", "Parul", "Aman", "Parul", "Sahil"]
count = 0
for i in names:
    if i.lower() == "parul":
        count+= 1
print("no of times parul appear:", count)

#find the index of "Sahil", and reverse the list.
index_val = names.index('Sahil')
print("index value of Sahil is :",index_val)
names.reverse()
print(names)

#4.Write a program to create a list and print the first 3 items,
# the last 2 items, and all items at even positions.
l = [0,1,2,3,4,5,6]
print(l[0:3])
print(l[-2:])
print(l[::2])

#5.Given a list: nums = [1, 4, 7, 10, 13],
# print the square of each element using a loop,
# and create a new list of only even numbers.
nums = [1, 4, 7, 10, 13]
squares = []
for i in nums:
    z = i**2
    squares.append(z)
print("squares of numbers:",squares)
#create a new list of only even numbers
even = []
for i in nums:
    if i % 2==0:
        even.append(i)
print("new list of even number is :",even)

#6.Write a program to find the largest number in a list without using the max() function.
l = [40,60,50,34,67,20,67,90,54]
l.sort()
print("the largest number is:",l[-1])
# another way without sort buildin fun:
l = [40,60,50,34,67,20,67,90,54]
largest_num = l[0]
for i in l:
    if i > largest_num:
        largest_num = i
print("largest no is :",largest_num)

#8.Given a list: [5, 2, 9, 1, 5, 6],
# remove all duplicates and print the list in ascending order.
list_1 = [5, 2, 9, 1, 5, 6]
print(sorted(set(list_1)))# to remove duplicates use set()

# without the use of set:
list_1 = [5, 2, 9, 1, 5, 6]
numbers = []
for i in list_1:
    if i not in numbers:
        numbers.append(i)
print("list after duplicates:",numbers)

#9.Take a sentence input from the user
# and convert it into a list of words using the `.split()` method.
text = input("enter the sentence:")
res = list(text.split())
print("The list of words :",res)

#10. Write a program to check
# if a list is a palindrome or not.)
numb = input("enter the numbers:")
res = list(numb.split())
print(res)

reverse_list = numb[::-1]
if numb == reverse_list:
    print("its a palindrome list")

else:
    print("it is not a palindrome list")






