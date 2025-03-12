package org.reflection;

import org.reflection.data.ExampleData;

public class BasicV1 {
    public static void main(String[] args) throws ClassNotFoundException {

        //클래스 메타데이터 조회 방법 3가지

        // 1. 클래스에서 찾기
        Class<ExampleData> basicData = ExampleData.class;

        System.out.println(basicData);


        // 2. 인스턴스에서 찾기
        ExampleData exampleData1 = new ExampleData();
        Class<? extends ExampleData> aClass = exampleData1.getClass();
        System.out.println(exampleData1.getClass());

        // 3.글자로 찾기
        String className = "org.reflection.data.BasicData";
        Class<?> basicData3 = Class.forName(className);
        System.out.println(basicData3);



    }
}
