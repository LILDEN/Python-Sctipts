a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
if a == 0:
    (a1, b1, e1) = (a, b, e)
    (a, b, e) = (c, d, f)
    (c, d, f) = (a1, b1, e1)
# print(a, b, c, d, e, f, sep=" ")
if c != 0:
    multUp = c
    multDown = a
    (c, d, f) = (c * multDown, d * multDown, f * multDown)
    (a, b, e) = (a * multUp, b * multUp, e * multUp)
    (c, d, f) = (c - a, d - b, f - e)
if b != 0:
    multUp = d
    multDown = b
    (a, b, e) = (a * multUp, b * multUp, e * multUp)
    (c, d, f) = (c * multDown, d * multDown, f * multDown)
    (a, b, e) = (a - c, b - d, e - f)
y = f / d
x = e / a
print(x, y)
