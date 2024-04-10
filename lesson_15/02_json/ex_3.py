import json

data = {
    'developer':
        {
            'name': 'Сергій',
            'positions': 'Senior Developer'
        }
}
with open('data_user.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)


with open('data_user.json', 'r', encoding='utf-8') as f:
    restored_data = json.load(f)
    print(restored_data)
