# I choose 4.13
buffet_food = ("Pizza", "Burgers", "Fish", "Hushpuppies", "Pudding")
print("The Original Menu:")
for buffet in buffet_food:
    print(buffet)

# Here i did dimensions[0] = bruh and it created a tuple error

revisedBuffet_food = ("Pizza", "Burgers", "Fish", "Hot Dogs", "Oysters")
print("The Modified List:")
for revised in revisedBuffet_food:
    print(revised)




# The second program is 4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
second_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

# Time to print!!!
for food in my_foods:
    print("The first food list is...", food)

# Time to print the second list!
for second in second_foods:
    print("\nThe second food list is...", second)





# The third program I choose is 4.11
pizza_list = ['Sausage Pizza', 'Pepperoni Pizza', 'Taco Pizza',]
friend_pizzas = ['Sausage Pizza', 'Pepperoni Pizza', 'Taco Pizza',]

# Adding pizzas to pizza_list
pizza_list.append('Anchovies Pizza')

# Adding pizzas to the friend_pizza list
friend_pizzas.append('Pineapple Pizza')

# Using print and for loop for my list
for pizzas in pizza_list:
    print("My favorite pizzas are:",pizzas)

# Using print and for loop for friend pizza list
for friends in friend_pizzas:
    print("\nMy friend's favorite pizzas are:",friends)



# Above is the code that is not up to the PEP 8 standard
# Bleow is how my three programs would look like under PEP 8

 buffet_food = (
    "Pizza",
    "Burgers",
    "Fish",
    "Hushpuppies",
    "Pudding"
)

print("The Original Menu:")
for item in buffet_food:
    print(item)

# Modify the tuple and print the updated list
revised_buffet_food = (
    "Pizza",
    "Burgers",
    "Fish",
    "Hot Dogs",
    "Oysters"
)

print("The Modified List:")
for item in revised_buffet_food:
    print(item)



# Program 4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
second_foods = [
    'pizza',
    'falafel',
    'carrot cake',
    'cannoli',
    'ice cream'
]

# Time to print!!!
for food in my_foods:
    print("The first food list is...", food)

# Time to print the second list!
for food in second_foods:
    print("\nThe second food list is...", food)



# Program 4.11
pizza_list = [
    'Sausage Pizza',
    'Pepperoni Pizza',
    'Taco Pizza'
]

friend_pizzas = [
    'Sausage Pizza',
    'Pepperoni Pizza',
    'Taco Pizza'
]

# Adding pizzas to pizza_list
pizza_list.append('Anchovies Pizza')

# Adding pizzas to friend_pizzas list
friend_pizzas.append('Pineapple Pizza')

# Using print and for loop for my list
for pizza in pizza_list:
    print("My favorite pizzas are:", pizza)

# Using print and for loop for friend pizza list
for friend_pizza in friend_pizzas:
    print("\nMy friend's favorite pizzas are:", friend_pizza)
