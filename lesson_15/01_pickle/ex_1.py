import pickle

d = {'some_key': 12345}
with open('ex_1_data.bin', 'wb') as file:
    pickle.dump(d, file)

d_bytes = pickle.dumps(d)
print(d_bytes)

with open('ex_1_data.bin', 'rb') as f:
    db = pickle.load(f)
print(db)

d_bytes_decode = pickle.loads(d_bytes)
print(d_bytes_decode)

# dump i load - використовуються при роботі із файлом
# dumps і loads - при передачі даних по мережі (дані зберігаються у памяті.)
