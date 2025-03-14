package org.annotation.mapping;

import java.lang.reflect.Method;

public class Main {
    public static void main(String[] args) {
        TestController controller = new TestController();

        Class<? extends TestController> aClass = controller.getClass();

        for(Method method: aClass.getDeclaredMethods()) {
            SimpleMapping annotation = method.getAnnotation(SimpleMapping.class);
            if (annotation != null) {
                System.out.println(annotation.value() + " => " + method);
            }
        }
    }
}
