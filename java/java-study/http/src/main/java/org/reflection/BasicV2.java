package org.reflection;

import org.reflection.data.ExampleData;

import java.lang.reflect.Modifier;

public class BasicV2 {

    public static void main(String[] args) {
        Class<ExampleData> basicDataClass = ExampleData.class;

        System.out.println(basicDataClass.getName());
        System.out.println(basicDataClass.getSimpleName());
        System.out.println(basicDataClass.getPackage());
        System.out.println(basicDataClass.getSuperclass());
        System.out.println(basicDataClass.isInterface());


        int m = basicDataClass.getModifiers();
        System.out.println(Modifier.toString(m));
    }
}
