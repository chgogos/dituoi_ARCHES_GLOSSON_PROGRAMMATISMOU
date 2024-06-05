#include <iostream>
using namespace std;

class A {
public:
  virtual void draw() { cout << "Object A: " << this << endl; }
};

class B : public A {
public:
  void draw() { cout << "Object B: " << this << endl; }
};

int main() {
  A *r = new A();
  r->draw();
  r = new B();
  r->draw();
}