while True:
    print("Εισάγετε έναν μη αρνητικό ακέραιο αριθμό: ", end="")
    n = input()
    if n.isdigit():
        n = int(n)
        if n >= 0:
            break
    print("Λάθος τιμή, προσπαθήστε ξανά!")

sum_ = 0.0
for i in range(n):
    sum_ += 1 / 2**i

print(f"Οι {n} πρώτοι όροι έχουν άθροισμα {sum_:.7}")
