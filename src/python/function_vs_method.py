# Συνάρτηση
def greet(name):
    return f"Hello, {name}!"


class Greeter:
    def __init__(self, name):
        self.name = name

    # Μέθοδος
    def greet(self):
        return f"Hello, {self.name}!"


print(greet("Alice"))  # Έξοδος: Hello, Alice!
g = Greeter("Bob")
print(g.greet())  # Έξοδος: Hello, Bob!
