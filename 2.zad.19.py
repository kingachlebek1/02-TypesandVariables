a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c))**(1/2)
print(f"Area: {area}")