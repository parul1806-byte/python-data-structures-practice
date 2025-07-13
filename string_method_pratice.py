#1️⃣ Take a string input and print its length.
a = 'parul'
print("length of a :",len(a))

#2️⃣ Print the first and last character of a string.
a = 'parul'
print("The frist and last character of the string is :",a[0],a[-1])

#3️⃣ Check if a string starts with "Hello".
s = "hello , how are you?"
print(s.startswith('hello'))

#4️⃣ Convert a string to uppercase and lowercase.
s = "hello , how are you?"
print("string in lower case:",s.lower())
print("string in upper case:",s.upper())

#5️⃣ Remove extra spaces from both ends of a string.
s = "  hello,how are you ?  "
print(s.strip())

#6️⃣ Given a string "PythonProgramming", print:First 6 letters,Last 5 letters,Every second letter,Reverse the string
s = "PythonProgramming"
print(s[:6])
print(s[-5:])
print(s[::2])
print(s[::-1])


#7️⃣ Concatenate two strings: "Data" and "Science"
d = "data"
s = "science"
print(d + " " + s)

#8️⃣ Repeat "Hello" 3 times using *
print("hello\t"*3)

#9️⃣ Check if the word "data" is present in the sentence
sen = "data science is fastest growing field in the IT sector"
new_sen = sen.lower().split()
if "data" in new_sen:
    print("present at the index:" , sen.find('data'))
else:
    print("not present")

#10️⃣ Count how many times 'a' appears in the string
sen = "data science is fastest growing field in the IT sector"
print("no of times a appear in te string:",sen.count('a'))


#11️⃣ Ask user to enter a string and print each character one by one (using for loop)
str = input("enter the string:")
for i in str:
    print(i)

# 12️⃣ Count how many vowels are there in the string
str = input("enter the string:")
str = str.lower()
count = 0
for i in str:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count += 1
print("no of vowels are :",count)

#13️⃣ Check if the string is a palindrome or not
text = input("enter the string:")
text = text.lower()
rev = text[::-1]
if rev == text:
    print("its a palindrome")
else:
    print("not a palindrome")

#14️⃣ Replace all spaces in a sentence with -
text = input("enter the string:")
print(text.replace(" ","-"))

 #15️⃣ Split a sentence into words and store them in a list
text = input("enter the string:")
text = text.split()
print(text)

#16️⃣ Find how many words are in the sentence
str = input("enter the string:")
length = len(str.split())
print("no words in the string:",length)

#17️⃣ Capitalize the first letter of each word in the string
str = input("enter the string:")
print(str.capitalize())

#18️⃣ Find the word with the maximum length in a sentence
str = input("enter the string:")
text = str.split()
longest = max(text,key=len)
print("the word with maximum len is :",longest)

# 19️⃣ Take name and age as input and print:
name = input("enter the user_name:")
age = input("enter the user_age:")
print("hello! {}, your age is {} .".format(name,age))

#20️⃣ Format a float value (like 3.14159) to 2 decimal places: 3.14
pi = 3.14159
print("pi = {:.2f}".format(pi))
