# maketrans
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
print(trantab)

str = "This is string example"
print(str.translate(trantab))