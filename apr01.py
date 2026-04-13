import random
words1 = ["cat", "dog", "apple", "cat"]
words2 = ["blue", "red", "yellow", "green", "brown"]
num1 = random.randint(10,99)
num2 = random.randint(10,99)

password = str(num1) + random.choice(words2) + random.choice(words1).upper()

test = "thIS is a class"
print(test.upper())
print(test.lower())
print(test.capitalize())
print(test.title())
print(test.swapcase())
s = "student"
print(s.capitalize().swapcase())













