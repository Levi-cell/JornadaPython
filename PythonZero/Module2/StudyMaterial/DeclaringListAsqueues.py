from collections import deque

queue = deque(["Eric", "John", "Michael"])

print(queue)
print("-" * 35)

queue.append("Terry")  # Terry arrives

print(queue)
print("-" * 35)

queue.append("Graham")  # Graham arrives

print(queue)
print("-" * 35)

queue.popleft()  # The first to arrive now leaves, Eric leaves

print(queue)
print("-" * 35)

queue.popleft()  # The second to arrive now leaves, John leaves

print(queue)
print("-" * 35)


