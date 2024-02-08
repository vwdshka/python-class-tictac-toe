import random

randomNumbers = random.sample(range(1, 1000), 10)
max = 0^10000000
min = 10^10000000

print("Before Sorting: ")
for i in range(randomNumbers.__len__()):
    print(randomNumbers[i], end=' ')

print("\n\nAfter Sorting: ")
for i in range(len(randomNumbers)-1):
    for j in range(len(randomNumbers)-1):
        if randomNumbers[j] > randomNumbers[j+1]:
            randomNumbers[j], randomNumbers[j+1] = randomNumbers[j+1], randomNumbers[j]

for i in range(randomNumbers.__len__()):
    print(randomNumbers[i], end=' ')

print("\n\nMax: ", randomNumbers[randomNumbers.__len__()-1])
print("Min: ", randomNumbers[0])
