from time import time
import resource  # бібліотека для того щоб перевірити скільки пам'яті використало


def read_file_yield(filename):
    text = open(filename, 'r')
    while True:
        line = text.readline()
        if not line:
            text.close()
            break
        yield line


start = time()
data = read_file_yield('data.txt')
# for l in data:
#     print(l)
diff = time() - start
print(diff)
print('Memory usage:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

# 0.2702000141143799
# Memory usage: 204 218 368
# 9.5367431640625e-07
# Memory usage: 9 547 776