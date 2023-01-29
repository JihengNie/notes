# Slicing examples
s = "abcdefgh"
print("s:", s)
print("s[3:6]", s[3:6])
print("s[3:6:2]", s[3:6:2])
print("s[::]", s[::])
print("s[::-1]", s[::-1])
print("s[4:1:-2]", s[4:1:-2])

# Robot Cheerleader
# an_letters = "aefhilmnorsxAEFHILMNORSX"

# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiam level (1-10): "))

# for char in word:
#   if char in an_letters:
#     print("Give me an " + char + "! " + char)
#   else:
#     print( "Give me a " + char + "! " + char)
# print("What does that spell?")
# for i in range(times):
#   print(word, "!!!")

# Exercise
s1 = "mit u rock"
s2 = "i rule mit"
if len(s1) == len(s2):
  for char1 in s1:
    for char2 in s2:
      if char1 == char2:
        print("common letter", char1)
        break

# Guess and check for cube root
cube = 8
for guess in range(abs(cube)+1):
  if guess ** 3 >= abs(cube):
    break

if guess ** 3 != abs(cube):
  print(cube, 'is not a perfect cube')

else:
  if cube < 0:
    guess = -guess
    print('Cube root of ' + str(cube) + ' is ' + str(guess))

# Approximation method
cube = 27
epsilon = .01
guess = 0.0
increment = 0.0001
num_guesses = 0

while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
  guess += increment
  num_guesses += 1
print("num_guesses =", num_guesses)

if abs(guess ** 3 - cube) >= epsilon:
  print("Failed on cube root of ", cube)
else:
  print(guess, "is close to the cube root of", cube)

# Bisection search
cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0

while abs(guess ** 3 - cube) >= epsilon:
  if guess ** 3 < cube:
    low = guess
  else:
    high = guess
  guess = (high + low) / 2.0
  num_guesses += 1
print("num_guesses =", num_guesses)
print(guess, "is close to the cube root of", cube)
