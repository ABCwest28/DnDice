from random import randrange

A = dict(zip(list(range(3, 19)), [0]*16))
B = dict(zip(list(range(18, 109)), [0]*91))
sum1 = 0
sum6 = 0

while True:
    try:
        n_iteration = int(input("Введите кол-во бросков:"))
        break
    except:
        print("не целое число")

for i in range(n_iteration):
    numbers = [randrange(1, 7) for _ in range(4)]
    numbers.sort(reverse=True)
    sum1 = sum(numbers[:3])
    A[sum1] += 1
    sum6 += sum1
    if (i+1)%6 == 0:
        B[sum6] += 1
        sum6 = 0
for key in A:
    print(key, A[key])
print('\n')
for key in B:
    print(key, B[key])
print('\n')