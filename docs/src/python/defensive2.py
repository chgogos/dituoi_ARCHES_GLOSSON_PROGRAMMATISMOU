while True:
    x = input("Δώσε θετικό ακέραιο αριθμό: ")
    try:
        if int(x) <= 0:
            print('Λάθος είσοδος, δοκιμάστε ξανά')
        else:
            break
    except ValueError:
        print('Λάθος είσοδος, δοκιμάστε ξανά')

print(x)
