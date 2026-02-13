import random
import re

random.seed(2025)


def generate_random_text(n):
    greek_lowercase = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    greek_uppercase = greek_lowercase.lower()
    digits = "0123456789"
    all_chars = greek_lowercase + greek_uppercase + digits
    random_text = "".join(random.choice(all_chars) for _ in range(n))
    return random_text


def inject_multiplications(txt, n):
    assert len(txt) >= 20, "the text's length must be at least 20 characters"
    for _ in range(n):
        x = random.randint(0, 99)
        y = random.randint(0, 99)
        to_be_injected = f"ΠΟΛΛΑΠΛΑΣΙΑΣΕ({x},{y})"
        pos = random.randint(0, len(txt) - len(to_be_injected))
        # print(f"{to_be_injected} εισαγωγή στη θέση {pos}")
        txt = txt[:pos] + to_be_injected + txt[pos + len(to_be_injected) :]
    return txt


def compute(txt):
    results = re.findall(r"ΠΟΛΛΑΠΛΑΣΙΑΣΕ\((\d{1,2}),(\d{1,2})\)", txt)
    total = 0
    for x in results:
        total += int(x[0]) * int(x[1])
    return total


def scenario1():
    txt = generate_random_text(100)
    print(txt)

    print("#" * 80)
    txt2 = inject_multiplications(txt, 3)
    print(txt2)

    result = compute(txt2)
    print("Αποτέλεσμα = ", result)


def scenario2():
    txt = generate_random_text(50_000)

    txt2 = inject_multiplications(txt, 500)
    with open("test_multiplications1.txt", "w") as f:
        f.write(txt2)

    result = compute(txt2)
    print("Αποτέλεσμα = ", result)


if __name__ == "__main__":
    scenario1()
    # scenario2()
