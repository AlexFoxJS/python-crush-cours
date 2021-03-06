# Перебор значений Словарей
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c++',
#     'edward': 'ruby',
#     'phil': 'python',
#     'alex': 'python'
# }

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    'alex': ['python', 'ecma']
}

print('')

# for name, lang in favorite_languages.items():
#     print(name.title() + " favorite language is " + lang.title() + ".")

# for name in favorite_languages:
#     print(name)

# for name in favorite_languages.keys():
#     print(name)

# for val in favorite_languages.values():
#     print(val)

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#
#     if name in friends:
#         print("    Hi " + name.title() + ", I see your favorite language is "
#               + favorite_languages[name].title() + "!")

# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")

    for language in languages:
        print("\t" + language.title())

print('')
