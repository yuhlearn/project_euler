from time import time

def sign(x, y, z):
    return (x[0] - z[0])*(y[1] - z[1]) - (y[0] - z[0])*(x[1] - z[1])

def point_in_triangle(pt, x, y, z):
    b1 = sign(pt, x, y) < 0.0
    b2 = sign(pt, y, z) < 0.0
    b3 = sign(pt, z, x) < 0.0
    return (b1 == b2) and (b2 == b3)

start = time()

f = open('p102_triangles.txt')
points = [zip(*[iter(map(int, l.split(',')))]*2) for l in f.readlines()]
f.close()

print 'Time:', time() - start
print [point_in_triangle((0, 0), x, y, z) for x, y, z in points].count(True)
