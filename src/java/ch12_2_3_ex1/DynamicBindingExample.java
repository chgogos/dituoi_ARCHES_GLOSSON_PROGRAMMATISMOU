package ch12_2_3_ex1;

class A {
    public void draw() {
        System.out.println("Object A: " + this);
    }
}

class B extends A {
    public void draw() {
        System.out.println("Object B: " + this);
    }

}

public class DynamicBindingExample {
    public static void main(String[] args) {
        A ref = new A();
        ref.draw();
        ref = new B();
        ref.draw();
    }
}