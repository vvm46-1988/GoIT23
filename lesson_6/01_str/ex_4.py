data_str = "зюсбщ"

symbol_map = {
    ord('ю'): 'u',
    ord('б'): 'b',
    ord('с'): 's',
    ord('ш'): 'sh',
    ord('щ'): 'shch',
}

print(symbol_map)
new_str = data_str.translate(symbol_map)
print(new_str)