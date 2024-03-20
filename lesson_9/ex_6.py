"""
FIFO (англ. first in, first out - "першим прийшов - першим пішов") - спосіб організації даних або іншими словами черга.
Цей вислів описує принцип технічної обробки черги або обслуговування конфліктних вимог шляхом упорядкування процесу
за принципом: "першим прийшов - першим обслужений".
Той, хто приходить першим, той і обслуговується першим, хто прийде наступним чекає,
поки обслуговування першого не буде закінчено, і так далі.
"""

from collections import deque

MAX_LEN = 5

fifo = deque(maxlen=MAX_LEN)

def push(el):
    fifo.append(el)

def pop():
    return fifo.popleft()

push('Svitlana')
push('Ivan')
push('Petro')
push('Vova')
push('Ihor')

print(fifo)
name = pop()
print(name)
print(fifo)
