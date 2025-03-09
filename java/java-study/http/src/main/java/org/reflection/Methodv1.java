package org.reflection;

import org.reflection.data.BasicData;

import java.lang.reflect.Method;

public class Methodv1 {

    public static void main(String[] args) throws ClassNotFoundException {
        String className = "org.reflection.data.BasicData";
        Class<?> basicDataClass = Class.forName(className);

        // public인 상속 포함 모든 메소드
        System.out.println("###############method##################");
        Method[] methods = basicDataClass.getMethods();

        for (Method method: methods) {
            System.out.println("method: " + method);
        }

        //해당 클래스에서만 선언한 메서드들(상속 제외)
        System.out.println("###############method##################");
        Method[] declaredMethods = basicDataClass.getDeclaredMethods();
        for (Method method: declaredMethods) {
            System.out.println("method: " + method);
        }

    }
}
