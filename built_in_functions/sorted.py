more_numbers = [6, 1, 8, 2]
print(sorted(more_numbers))
print(more_numbers)
print(more_numbers.sort())
print(more_numbers)
print(sorted(more_numbers, reverse=True))
users = [
    {"username": "samuel", "tweets": [
        "I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

print(sorted(users, key=lambda user: user['username']))
print("-------")
print(sorted(users, key=lambda user: len(user['tweets'])))
print("-------")
songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]
print(sorted(songs, key=lambda songs: songs['playcount'], reverse=True))
