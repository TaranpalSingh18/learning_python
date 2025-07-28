from collections import namedtuple

Point = namedtuple('Point','x,y')
point = Point(-1,5)
print(point.y, point.x)