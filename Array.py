fruits = ["Orange", "Banana", "Kiwi", "Mango", "Watermelon"]
print(fruits[1])

fruits.pop(1)
print(fruits);

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

if "Banana" in fruits:
    print("Yes, Banana is in the list")
else:
    print("Sorry, Banana doesnt exist in the list")

print(len(fruits))

for fruit in fruits:
    print(fruit.upper())