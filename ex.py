n = int(input())

s = 0



t = n

while t > 0:

   digit = t % 10

   s += digit ** 3

   t //= 10

print(s)

