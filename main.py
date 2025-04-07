users:list[dict] = [
    {'name': 'Kinga', 'location': 'Kozienice', 'posts': 500, },
    {'name': 'Wika', 'location': 'Radzyń', 'posts': 400, },
    {'name': 'Daria', 'location': 'Łosice', 'posts': 200, }
]

for user in users:
    print(f'Twój znajomy: {user["name"]} z {user["location"]} opublikował {user["posts"]}')
