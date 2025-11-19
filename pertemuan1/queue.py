queue = []

queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

element = queue.pop(0)
print("Dequeue: ", element)

frontElement = queue[0]
print("Peek: ", frontElement)

isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

print("Size: ", len(queue))