# interative method

def fact(x):
  k = x
  for x in range(1,x):
    k = k * x
  return k

# recursive method

def recursiveFact(x):
  if x == 1:
    return 1
  else:
    return x * recursiveFact(x-1)


print(f"Factorial Algorithm\n")
print(f"========================================\n")
x = True
while(x):
  try:
    number = int(input(f"Please enter an integer -> "))
    x = False
  except:
    print(f"Please, try again, integer number only \n")
# measure initial time
st = time.time()
print(f"\nFactorial of {number} is {fact(number)}")
ed = time.time()
print(f"\nTime spent in calculation {(ed-st)*1000} ms")
st = time.time()
print(f"\nRecursive Factorial of {number} is {recursiveFact(number)}")
ed = time.time()
print(f"\nTime spent in calculation is {(ed-st)*1000} ms")
