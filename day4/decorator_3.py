def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b # a = (b , a + b)
    n = n + 1
  return 'done'

res = fib(10)
print(res.__next__())

# 异常
# try:
#   pass
# except expression as identifier:
#   pass 