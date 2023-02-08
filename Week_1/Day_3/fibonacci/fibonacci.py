def fibonacci(n):
  fib_arr = [0, 1]
  
  if n == 0 or n == 1:
    return fib_arr[n]

  count = 2
  while count <= n:
    fib_arr.append(fib_arr[-1] + fib_arr[-2])
    count += 1
  
  return fib_arr[-1]




print(fibonacci(0) == 0)
print(fibonacci(2) == 1)
print(fibonacci(5) == 5)
print(fibonacci(8) == 21)
print(fibonacci(11) == 89)
print(fibonacci(14) == 377)
print(fibonacci(17) == 1597)
print(fibonacci(20) == 6765)