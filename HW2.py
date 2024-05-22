# Homework 2

### Use Input/Output (input/print) for all questions

## Basic Exercises

#1. **Age Calculation**

#   - Create a program to ask for the user's name and year of birth, then tell them their age.
   
name = input("what is your name?")
yob = int(input("yob:"))
print(f"{name}, you are {2024-yob} years old")

#2. **Extract Car Names**
#   - Extract car names from this text:
txt = 'LMaasleitbtui'
print(txt[0::2])
print(txt[1::2])

#3. **Extract Car Names**
#   - Extract car names from this text:
txt = 'MsaatmiazD'
print(txt[0::2])
print(txt[-1::-2])

#4. **Extract Residence Area**
# - Extract the residence area from this text:
txt = "I'am John. I am from London"
print(txt[-6:])
print(txt[len(txt)-6:])


## Optional (For Wonderkids)

#1. **String Reversal**
#   - Create a program that takes a string input from the user and prints the string in reverse.
string = input("enter your string: ")
print(f"your reversed string is {string[::-1]}")

#2. **Vowel Counter**
#   - Create a program that counts the number of vowels (a, e, i, o, u) in a given string.
string = input("enter your string: ")
vowels_count=0
for i in string:
    if i in 'aeiou':
        vowels_count+=1
print(f"number of vowels here is {vowels_count}")

#3. **Sum of Digits**
#   - Create a program that takes an integer input from the user and calculates the sum of its digits.
num = input("enter your number: ")
sum = 0
for digit in num:
        sum += int(digit)
print(f"sum of your digits is: {sum}")

#4. **String Palindrome**
#   - Create a program that checks if a given string is a palindrome.
text = input("enter your string: ")
if text[::-1]==text[::]:
    print("palindrome")
else:
    print("not palindrome")

#5. **Character Frequency**
#   - Create a program that counts the frequency of each character in a given string.
string = input("Enter your string: ")
char_freq = {}
for char in string:
    if char not in char_freq:
        count = string.count(char)
        if count > 0:
            print(f"{char}'s frequency is {count}")
        char_freq[char] = count