import random

queue = []
list_entries = 10
number_range = 100

for value in range(list_entries):
    queue.append(random.randint(0, number_range))

print(queue)

while len(queue) != 0:
    
    print("Current number is", queue.pop(0), "and the queue is", queue)

print("The list is now empty")
