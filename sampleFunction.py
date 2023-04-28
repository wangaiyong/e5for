from random import randint, sample
date = [randint(10,20) for _ in range(10)]
c = sample(date, 5)
print(c)
