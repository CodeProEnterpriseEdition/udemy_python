user_info = {'name':'hemuli', 'malli':'muumi', 'laakso': 'iso-laakso'}
print(user_info)

print(user_info['name'])
artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name = f"{artist['first']} {artist['last']}"
print(full_name)

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0
for value in donations.values():
    total_donations += value
print(total_donations)
total_donations = sum(donation for donation in donations.values())
print(total_donations)
total_donations = sum(donations.values())
print(total_donations)

print('sam' in donations)
print('peruna' in donations)

print(25.0 in donations.values())
print(23 in donations.values())

copy = artist.copy()

print(copy == artist)
print(copy is artist)

new_user = {}.fromkeys(['name', 'score', 'email'], 'unknown')
print(new_user)
new_user.update({'name':'hemuli'})
print(new_user)
print(new_user.get('name'))
print(new_user.get('name2'))

from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
print(food)
# for key,value in bakery_stock.items():
#     if food == key:
#         print("{} left".format(value))
#     else:
#         print("we don't make that")

if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")

quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")

game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state = dict.fromkeys(game_properties, 0)
print(game_properties)
print(initial_game_state)