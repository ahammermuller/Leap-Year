# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = name1 + name2

names = names.lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
true = str(t+r+u+e)

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")
love = str(l+o+v+e)

score = true + love
score = int(score)

if score <10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif 40 <= score <=50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')


