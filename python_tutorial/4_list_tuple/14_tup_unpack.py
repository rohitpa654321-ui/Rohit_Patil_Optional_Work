fruits = ("apple","banana","cherry","kiwi","mango","orange","papaya")
(green, yellow, *red) = fruits
print("1. ",green)
print("2. ",yellow)
print("3. ",red)

(green, *yellow, red) = fruits
print("\n4. ",green)
print("5. ",yellow)
print("6. ",red)

