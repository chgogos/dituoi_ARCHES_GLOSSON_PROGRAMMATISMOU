package ch12_6_3_ex1;

import java.lang.reflect.*;

public class ReflectTest {
    public static void main(String[] args) {
        Object[] birdList = new Object[3];
        birdList[0] = new Bird1();
        birdList[1] = new Bird2();
        birdList[2] = new Bird3();
        Reflect.callDraw(birdList[2]);
        Reflect.callDraw(birdList[0]);
        Reflect.callDraw(birdList[1]);
    }
}

class Reflect {
    public static void callDraw(Object birdObj) {
        Class cls = birdObj.getClass();
        try {
            Method method = cls.getMethod("draw");
            method.invoke(birdObj);
        } catch (NoSuchMethodException e) {
            throw new IllegalArgumentException(cls.getName() + " does not support draw");
        } catch (IllegalAccessException e) {
            throw new IllegalArgumentException(
                    "Insufficient accesss permissions to call draw in class " + cls.getName());
        } catch (InvocationTargetException e) {
            throw new RuntimeException();
        }
    }
}

class Bird1 {
    public void draw() {
        System.out.println("This is a draw from Bird1");
    }
}

class Bird2 {
    public void draw() {
        System.out.println("This is a draw from Bird2");
    }
}

class Bird3 {
    public void draw() {
        System.out.println("This is a draw from Bird3");
    }
}
