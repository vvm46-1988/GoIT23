from time import time
import resource  # бібліотека для того щоб перевірити скільки пам'яті використало

def read_file(filename):
    text_file = open(filename, 'r')
    lines = text_file.readlines()
    text_file.close()
    return lines


start = time()
data = read_file('data.txt')
# for l in data:
#     print(l)
diff = time() - start
print(diff)
print('Memory usage:', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

# 0.2702000141143799
# Memory usage: 204218368

