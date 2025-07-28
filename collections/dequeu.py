from collections import deque

d = deque()
d.append(3)
d.append(4)

d.appendleft(10)

d.pop()
d.popleft()

d.append(10)
d.append(4)
print(d)

d.rotate(-2)


print(d)