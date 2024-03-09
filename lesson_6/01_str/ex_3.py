"""
Метод: split, join
----
"""

url_query = url_search = "https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"

value, query = url_search.split('#')
# print(value)
print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)