# extend
language_1 = ["C", "C++", "Java", "Python", "Rust"]
language_2 = ["TypeScript", "PHP", "Python", "Go"]


# language_1.append(language_2)
language_1.extend(language_2)
print(language_1)
language_1 += language_2
print(language_1)