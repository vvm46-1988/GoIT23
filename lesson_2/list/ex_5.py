# Списки списків
language_1 = ["C", "C++", "Java", "Python", "Rust", ["JS", "mojo"]]
language_2 = ["TypeScript", "PHP", "Python", "Go"]
language_3 = [language_1, language_2]

print(language_3)
# print(language_3[0][5][0])
print(language_3[0][5].index('mojo'))
print('JS' in language_3[0][5])