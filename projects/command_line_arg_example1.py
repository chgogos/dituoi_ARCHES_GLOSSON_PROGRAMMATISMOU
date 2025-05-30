import sys


if __name__ == "__main__":
    print(f"ΠΛΗΘΟΣ ΟΡΙΣΜΑΤΩΝ: {len(sys.argv)}")
    for i, argv in enumerate(sys.argv):
        print(f"όρισμα {i} με τιμή {argv}")
