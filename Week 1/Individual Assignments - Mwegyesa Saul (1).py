import random

# Exercise 1: Lists
names = ["John", "Jane", "David", "Sarah", "Michael"]
print(names[1])

names[0] = "Peter"
print(names)

names.append("Emily")
print(names)

names.insert(2, "Bathel")
print(names)

del names[3]
print(names)

print(names[-1])

new_list = [10, 20, 30, 40, 50, 60, 70]
print(new_list[2:5])

countries = ["USA", "UK", "Canada", "Australia"]
countries_copy = countries.copy()
print(countries_copy)

for country in countries:
    print(country)

animal_names = ["Lion", "Tiger", "Elephant", "Giraffe", "Monkey"]
animal_names.sort()
print(animal_names)
animal_names.sort(reverse=True)
print(animal_names)

animal_names_with_a = [name for name in animal_names if 'a' in name.lower()]
print(animal_names_with_a)

first_names = ["John", "Jane", "David"]
second_names = ["Doe", "Smith", "Johnson"]
joined_names = first_names + second_names
print(joined_names)


# Exercise 2: Tuples
x = ("samsung", "iphone", "tecno", "redmi")
print(x[1])

print(x[-2])

x = list(x)
x[1] = "itel"
x = tuple(x)
print(x)

x = x + ("Huawei",)
print(x)

for item in x:
    print(item)

x = x[1:]
print(x)

uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara"])
print(uganda_cities)

a, b, c, d = uganda_cities
print(a, b, c, d)

print(uganda_cities[1:4])

first_names = ("John", "Jane", "David")
second_names = ("Doe", "Smith", "Johnson")
joined_names = first_names + second_names
print(joined_names)

colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_of_eight = thistuple.count(8)
print(count_of_eight)


# Exercise 3: Sets
favorite_beverages = set(["coffee", "tea", "juice"])
print(favorite_beverages)

favorite_beverages.add("water")
favorite_beverages.update(["soda", "milk"])
print(favorite_beverages)

mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")

mySet.remove("kettle")
print(mySet)

for item in mySet:
    print(item)

set_of_items = {1, 2, 3, 4}
list_of_items = [3, 4]
set_of_items.update(list_of_items)
print(set_of_items)

ages = {25, 30, 35}
first_names = {"John", "Jane", "David"}
joined_set = ages.union(first_names)
print(joined_set)

# Exercise 4: Strings
integer_variable = 10
string_variable = " years old"
concatenated_string = str(integer_variable) + string_variable
print(concatenated_string)

txt = " Hello, Uganda! "
print(txt.strip())  # Output: "Hello, Uganda!"

print(txt.upper())  # Output: " HELLO, UGANDA! "

replaced_string = txt.replace("U", "V")
print(replaced_string)  # Output: " Hello, Vganda! "

y = "I am proudly Ugandan"
print(y[1:5])  # Output: " am "

x = 'All "Data Scientists" are cool!'
print(x)  # Output: All "Data Scientists" are cool!

# Exercise 5: Dictionaries
shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(shoes["size"])  # Output: 40

shoes["brand"] = "Adidas"  # Changing the value of "brand" key
print(shoes)

shoes["type"] = "sneakers"  # Adding a new key/value pair
print(shoes)

keys = list(shoes.keys())
print(keys)  # Output: ["brand", "color", "size", "type"]

values = list(shoes.values())
print(values)  # Output: ["Adidas", "black", 40, "sneakers"]

if "size" in shoes:
    print("The key 'size' exists in the dictionary.")

for key, value in shoes.items():
    print(key, ":", value)

del shoes["color"]  # Removing the key "color"
print(shoes)

shoes.clear()  # Emptying the dictionary
print(shoes)

my_dict = {"name": "John", "age": 30, "country": "USA"}
my_dict_copy = my_dict.copy()
print(my_dict_copy)

nested_dict = {
    "person1": {"name": "John", "age": 30},
    "person2": {"name": "Jane", "age": 25}
}
print(nested_dict)

