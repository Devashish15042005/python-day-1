def fibonacci(n):
 a,b=0,1
 series = []
 for _ in range(n):
  series.append(a)
  a, b=b,a+b
 return series
terms =int(input("enter number for terms:"))
print("fibonacci series",fibonacci(terms))