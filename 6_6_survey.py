favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

users = ['jen', 'bob', 'curry', 'phil']

for user in users:
    if user in favorite_languages.keys():
        print(f"{user}, Thanks!")
    else:
        print(f'Invite {user} to join us!')
