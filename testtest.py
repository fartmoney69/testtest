# step 1: make a list of five cities
cities = ["New York", "Los Angeles", "Chicago", "Boston", "San Diego"]

# step 2: traverse the city list, printing out every name one after the other
for city in cities:
    print(city)

# step 3: allow the user to append a new city to the list
new_city = input("Enter a new city to add to the list: ")
cities.append(new_city)

# step 4: allow the user to delete a city from the list
del_city = int(input("Enter an index of the city to delete from the list: "))
del cities[del_city]

# step 5: print the list of cities to show these changes
print("The updated list of cities is:")
print(cities)