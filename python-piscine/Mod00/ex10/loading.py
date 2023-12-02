from tqdm import tqdm
from time import sleep

def process_list(iterable):
    return tqdm(iterable, desc="Processing")

listy = range(1000)
ret = 0
for elem in process_list(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print(ret)

listy = range(3333) 
ret = 0
for elem in process_list(listy): 
    ret += elem
    sleep(0.005) 
print()
print(ret)