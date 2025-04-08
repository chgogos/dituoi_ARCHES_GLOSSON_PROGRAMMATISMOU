public class Example1 {
    public static void foo(int x) {
        x++;
    }

    public static void bar(MyClass obj) {
        obj.a++;
        obj = new MyClass(77); // τροποποίηση της τοπικής μεταβλητής obj (ωστόσο, δεν επιτρέπεται η
                               // επαναπρόσδεσή της)
        System.out.println(obj.a);
    }

    public static void main(String[] args) {
        int x = 5;
        // μεταβίβαση κατά τιμή
        foo(x);
        System.out.println(x); // εμφανίζει 5

        MyClass obj = new MyClass(5);
        // προσομοίωση μεταβίβασης κατά αναφορά
        bar(obj);
        System.out.println(obj.a); // εμφανίζει 6 και όχι 77
    }

}

class MyClass {
    public int a;

    public MyClass(int a) {
        this.a = a;
    }
}