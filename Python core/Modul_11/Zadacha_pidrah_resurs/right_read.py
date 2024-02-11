from time import time
import resource  # працює тільки з UNIX


def read_file_yield(filename):
    text_file = open(filename, 'r')
    while True:
        line = text_file.readline()
        if not line:
            text_file.close()
            break
        yield line


start = time()
data = read_file_yield('data.txt')
# for line in data:
#     print(f"line: {line}")
print(time() - start)
print('Memory usage: ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

# 0.0
# Memory usage:  7 344 128


# Simple read
# 0.30776500701904297
# Memory usage:  231 473 152