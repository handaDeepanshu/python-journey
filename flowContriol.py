age = int(input("Enter Age: "))
if age < 13:
    print("You are child")
elif age < 18:
    print("You are teenager")
elif age < 25:
    print("You are young adult")
else:
    print("You are adult")

count  = 1
while count <= 8:
    print("Count: ", count)
    count += 1

fruits = ["apple", "mango","grapes", "orange"]
for fruit in fruits:
    print(fruit)

for i in range(1,11):
    print(i, end=" ")
print()

for i in range(1,20):
    if i % 2 == 0:
        continue
    if i > 10:
        break
print(i, end = " ")