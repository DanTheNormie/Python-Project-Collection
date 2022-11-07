"""
try:
    file = open("a.txt")
    dict = {'key':'value'}
    print(dict["no_key"])
except FileNotFoundError:
    print("File not Found")
except KeyError:
    print("Key not found")
else:
    print("Everything works")

print("This line prints")
"""


"""
fruits = ["Apple", "Orange", "Banana", "Pear"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + "pie")


make_pie(4)

"""

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

"""total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0
"""
"""
facebook_posts[3]["Likes"] = 0

print(facebook_posts[3]["Likes"])
"""