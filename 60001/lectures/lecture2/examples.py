# String concatnation
hi = "Hello there"
name = "ana"
greet = hi + " " + name

print(greet)

silly = hi + (" " + name) * 3

print(silly)

# output using print
x = 1
print(x)
x_str = str(x)
print("my fav num is", x, ".", "x =", x)
print("my fav num is " + x_str + ". " + "x = " + x_str)

# Comparision example
pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)
derive = True
drink = False
both = drink and derive
print(both)

# for loops examples
mysum = 0
for i in range(7, 10):
  mysum += i
print(mysum)


mysum = 0
for i in range(5, 11, 2):
  mysum += i
print(mysum)

# What will happen example
mysum = 0
for i in range(5, 11, 2):
  mysum += i
  if mysum == 5:
    mysum += 1
print(mysum)
