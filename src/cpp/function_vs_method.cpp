#include <iostream>
#include <string>

// Συνάρτηση
std::string greet(const std::string& name) { return "Hello, " + name + "!"; }

class Greeter {
 private:
  std::string name;

 public:
  Greeter(const std::string& name) : name(name) {}

  // Μέθοδος
  std::string greet() const { return "Hello, " + name + "!"; }
};

int main() {
  std::cout << greet("Alice") << std::endl;  // Έξοδος: Hello, Alice!
  Greeter g("Bob");
  std::cout << g.greet() << std::endl;  // Έξοδος: Hello, Bob!
  return 0;
}
