import json
from csv import DictReader

with open("users.json", "r") as json_file:
    users = json.loads(json_file.read())


users_list = []
for user in users:
    key = ['name', 'gender', 'address', 'age', 'books']
    value = [user['name'], user['gender'], user['address'], user['age'], []]
    user_dict = {k: v for k, v in zip(key, value)}
    users_list.append(user_dict)


with open("books.csv", newline="") as csv_file:
    reader = DictReader(csv_file)
    books = list(reader)


books_list = []
for book in books:
    key = ['title', 'author', 'pages', 'genre']
    value = [book['Title'], book['Author'], book['Pages'], book['Genre']]
    book_dict = {k: v for k, v in zip(key, value)}
    books_list.append(book_dict)


n = 0
users_len = len(users_list) - 1

for book in books_list:
    user = users_list[n]
    user['books'].append(book)
    if n <= users_len - 1:
        n += 1
    else:
        n = 0


with open("result.json", "w") as file:
    res = json.dumps(users_list, indent=4)
    file.write(res)
