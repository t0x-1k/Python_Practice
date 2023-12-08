# creating a mapping of stat to abbrevation
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

#create a basic set of states and some cities in them
cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville",
}

# Adding more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

#printing cities
print('-' * 15)

print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])

print('-' * 15)

print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

print('-' * 15)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated")

print('-' * 15)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 15)
state = states.get("Texas")

city = cities.get("TX", "Does not exist")
print(f"The city for the state 'TX' is: {city}")