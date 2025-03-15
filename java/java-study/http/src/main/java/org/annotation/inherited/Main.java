package org.annotation.inherited;

import java.lang.annotation.Annotation;

public class Main {


    static class A {

        void call() {
            System.out.println("A.class");
        }

    }

    static class B extends A{

        @Override
        void call() {
            System.out.println("B.class");
        }
    }


    public static void main(String[] args) {


//        Annotation[] annotations = TestInterfaceImpl.class.getAnnotations();
//
//        for (Annotation annotation: annotations) {
//            System.out.println(annotation);
//        }

        A b = new B();
        b.call();

    }
}
