# The list and printing list
candy_list = ['Gummy Bears', 'Candy Corn', 'Twix', 'Sour Patch Kids', 'Snickers', 'Hershys']

print("This is our list:",candy_list)

# Printing each item in the list individually
print(candy_list[0].title())
print(candy_list[1].title())
print(candy_list[2].title())
print(candy_list[3].title())
print(candy_list[4].title())
print(candy_list[5].title())

# Sorting the list by name
sortedCandy_list = sorted(candy_list)
print(sortedCandy_list)

# Printing the list and skipping a line
print("\n",candy_list[0].title())
print("\n",candy_list[1].title())
print("\n",candy_list[2].title())
print("\n",candy_list[3].title())
print("\n",candy_list[4].title())
print("\n",candy_list[5].title())

# Adding Mr. McKinstry's Favorite item
candy_list.append('McKinstry = Almond Joy')

# Printing in reverse order
candy_list.reverse()
print("\n",candy_list)

# Finding the Length of the list
print("\nThe length of the candy list is:",len(candy_list))




#################################################################################################################################################




# The practical test chapter 4
print("\nThe candy my group would like is Hershys from:", candy_list[1].title())


# The Second List 
cost_of_candy = ['\nAlmond Joy = $7', 'Hershys = $15', 'Snickers = $13', 'Sour Patch Kids = $7', 'Twix = $9', 'Candy Corn = $7']

# Concantinating 
cost_of_two = [
f"{candy_list[0]} {cost_of_candy[0].split('=')[1].strip()}",
f"{candy_list[1]} {cost_of_candy[1].split('=')[1].strip()}",
f"{candy_list[2]} {cost_of_candy[2].split('=')[1].strip()}",
f"{candy_list[3]} {cost_of_candy[3].split('=')[1].strip()}",
f"{candy_list[4]} {cost_of_candy[4].split('=')[1].strip()}",
f"{candy_list[5]} {cost_of_candy[5].split('=')[1].strip()}"
]

for cost in cost_of_candy:
    print(cost)

# Appending list 
alternate_candy = ['Gummy Bears', 'Candy Corn', 'Twix', 'Sour Patch Kids', 'Snickers', 'Hershys']

# Adding new candy
new_alternate_candy = ['KitKat', 'M&M']
alternate_candy.insert(1, new_alternate_candy[0])
alternate_candy.insert(2, new_alternate_candy[1])

# Taking out unavaliable candy
del alternate_candy[1]
del alternate_candy[2]

print("If item 2 is not avaliable, it's replaced with KitKat")
print("If item 3 is not avaliable, it's replaced with M&M")

# Final Results
print("\n",candy_list)
print("\n",alternate_candy)