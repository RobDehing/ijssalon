mijn_lijst = ["wafels", "Softijs", "Schepijs", "Pannekoeken"]
mijn_lijst.append("Muffins")
for item in mijn_lijst:
    print(f"Wij verkopen ", item)
print("-------------------------------------------------")
alfabet = ["A", "B", "D", "E", "F"]
print(alfabet)
alfabet.insert(2, "C")
print(alfabet)
print("-------------------------------------------------")
fruit = ["appel", "banaan", "kers"]
print("voor pop(1)", fruit)
fruit.pop(1)
print("Na pop(1)", fruit)
fruit.remove("kers")
print(fruit)
my_list_1 = ["appel", 2, True, "banaan"]
print("my-list = ", my_list_1)
# my_list.clear()
print("my-list = ", my_list_1)
print(my_list_1.count(2))
