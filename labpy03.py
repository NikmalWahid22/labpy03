import random

n = int(input("Masukkan nilai n: "))

i = 1

while i <= n:
    rand_num = random.random()
    if rand_num < 0.5:
        print(f"data ke: {i} => {rand_num}")
        i += 1

print("Selesai")
