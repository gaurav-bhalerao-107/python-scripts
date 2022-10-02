from cmath import sqrt

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = (b**2) - (4*a*c)

x1 = (-b+sqrt(d))/(2*a)
x2 = (-b-sqrt(d))/(2*a)
print(f"The solutions are {x1} and {x2}")
