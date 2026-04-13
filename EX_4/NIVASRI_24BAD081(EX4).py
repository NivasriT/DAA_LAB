print("NIVASRI T | 24BAD081")
print("STRASSEN'S ALGORITHM")
# Input matrix A
print("Enter elements of Matrix A:")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

# Input matrix B
print("Enter elements of Matrix B:")
e = int(input("e: "))
f = int(input("f: "))
g = int(input("g: "))
h = int(input("h: "))

# Strassen's 7 products
P1 = a * (f - h)
P2 = (a + b) * h
P3 = (c + d) * e

P4 = d * (g - e)
P5 = (a + d) * (e + h)
P6 = (b - d) * (g + h)
P7 = (a - c) * (e + f)

# Result matrix elements
C11 = P5 + P4 - P2 + P6
C12 = P1 + P2
C21 = P3 + P4
C22 = P1 + P5 - P3 - P7

# Display result
print("Resultant Matrix:")
print(C11, C12)
print(C21, C22)
