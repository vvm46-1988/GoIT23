"""
LIFO (англ. last in, first out, "останнім прийшов - першим пішов") - спосіб організації даних або іншими словами
Стек (Stack). У структурованому лінійному списку, організованому за принципом LIFO, елементи можуть додаватися та вибиратися з одного кінця, званого «вершиною списку».
"""

from collections import deque

MAX_LEN = 5

lifo = deque(maxlen=MAX_LEN)

def push(el):
    lifo.appendleft(el)  # O(1)


def pop():
    return lifo.popleft()

push('Svitlana')
push('Ivan')
push('Petro')
push('Vova')
push('Ihor')

print(lifo)
name = pop()
print(name)
print(lifo)
a = []
a.insert(0, 'Bohdan')  # O(n)