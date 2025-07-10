
#Q1. Create a tuple of 5 favorite fruits and print the third fruit.
fruits = ('apple','banana','mango','grapes','apricot')
print(fruits[2])

#Q2. Check if 'apple' exists in the tuple.
fruits = ('apple','banana','mango','grapes','apricot')
if 'apple' in fruits:
    print('yes')
else:
    print('no')

#Q3. Create a tuple with numbers and:Find its length,
# Print the last element using negative indexing
my_tuple = (10, 20, 30, 40, 50)
length = len(my_tuple)
print("length of the tuple:",length)
print("last element of the tuple:",my_tuple[-1])

#Q4. Convert a list ['dog', 'cat', 'fish'] into a tuple and print it.
animal = ['dog', 'cat', 'fish']
tup = tuple(animal)
print("list into tuple:",tup)

#Q5. Create two tuples:Concatenate them and print the result.
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print("tuple are Concatenate:",t3)


#Q6. Count how many times 7 appears in this tuple.
t = (7, 2, 9, 7, 5, 7)
print("The no of times 7 appear in the tuple:",t.count(7))

#Q7. Find the index of element 9 in the tuple
num = (1, 3, 9, 4, 9, 5)
print("The index value of 9 is :", num.index(9))

#Q8. Unpack the tuple into three separate variables and print each one.
items = (10,20,30)
a,b,c = items
print(a)
print(b)
print(c)


#Q9. Write a function that accepts a tuple of numbers and
# returns the sum of all values
digits = (input("input the number seprated by commas:"))
result = tuple( int(x) for x in digits.split(","))
print(sum(result))


#10. Given a tuple of mixed data:Print all items with their data types using a loop.
info = ('Parul', 21, 'Python', 98.5)
for item in info:
    print(f"{item} ->", type(item))

# 11 .Create a tuple of 10 numbers. Print all numbers greater than 50.
n = (10,20,30,40,50,60,70,80,90,100)
for i in n:
    if i > 50:
        print(i, end=" ")

#12 Take a tuple of numbers and create a new tuple of only even numbers.
n = (10,20,39,40,55,60,77,80,97,100)
even = []
for i in n :
    if i % 2 == 0:
        even.append(i)
even_num = tuple(even)
print(even_num)

#13.Convert a sentence into a tuple of words.
sen = input("enter the sentence:")
res = tuple(sen.split())
print(res)






