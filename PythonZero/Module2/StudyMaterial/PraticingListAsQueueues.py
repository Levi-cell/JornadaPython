print("Creating and Manipulating Stacks (LIFO)")
print("-" * 35)

stack = [3, 1, 5]

print("The stack is", stack)
print("-" * 35)

stack.append(2)

print("Now the stack is", stack)
print("-" * 35)

stack.pop()

print("Now the stack is", stack)
print("-" * 35)

# and Manipulating Queues (FIFO)
print("Creating and Manipulating Queues (FIFO)")
print("-" * 35)

from collections import deque

queue = deque([5, 8])

print("The queue is", queue)
print("-" * 35)

queue.append(10)

print("Now the queue is", queue)
print("-" * 35)

queue.popleft()

print("Now the queue is", queue)
print("-" * 35)

