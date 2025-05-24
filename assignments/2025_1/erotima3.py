from erotima1 import generate_random_text, inject_multiplications, compute
import time
import platform


def systeminfo():
    my_system = platform.uname()
    print(f"System: {my_system.system}")
    print(f"Node Name: {my_system.node}")
    print(f"Release: {my_system.release}")
    print(f"Version: {my_system.version}")
    print(f"Machine: {my_system.machine}")
    print(f"Processor: {my_system.processor}")


if __name__ == "__main__":
    systeminfo()
    n = 1_000_000
    m = 100_000
    start_time = time.time()
    txt = generate_random_text(n)
    end_time = time.time()
    print(f"ΧΡΟΝΟΣ ΔΗΜΙΟΥΡΓΙΑΣ ΑΡΧΙΚΟΥ ΚΕΙΜΕΝΟΥ {n} ΧΑΡΑΚΤΗΡΩΝ: {end_time - start_time:.2f} δευτερόλεπτα")

    start_time = time.time()
    txt = inject_multiplications(txt, m)
    end_time = time.time()
    print(
        f"ΧΡΟΝΟΣ ΕΙΣΑΓΩΓΗΣ {m} ΠΟΛΛΑΠΛΑΣΙΑΣΜΩΝ: {end_time - start_time:.2f} δευτερόλεπτα"
    )

    start_time = time.time()
    total = compute(txt)
    end_time = time.time()
    print(f"ΧΡΟΝΟΣ ΥΠΟΛΟΓΙΣΜΟΥ ΑΘΡΟΙΣΜΑΤΟΣ ΓΙΝΟΜΕΝΩΝ: {end_time - start_time:.2f} δευτερόλεπτα")

    print(f"ΣΥΝΟΛΙΚΟ ΑΘΡΟΙΣΜΑ ΓΙΝΟΜΕΝΩΝ = {total:,}")


