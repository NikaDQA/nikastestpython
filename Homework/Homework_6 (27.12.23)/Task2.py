for n in range(0, 51):
  def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
      d += 1
    return d * d > n

nums = list(filter(lambda n: IsPrime(n), range(0,51)))
print(nums)

def square(n):
  return n*n
print(list(map(square, nums)))