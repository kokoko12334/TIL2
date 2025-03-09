package org.reflection;

import org.reflection.data.BasicData;

public class BasicV1 {
    public static void main(String[] args) throws ClassNotFoundException {

        //클래스 메타데이터 조회 방법 3가지

        // 1. 클래스에서 찾기
        Class<BasicData> basicData = BasicData.class;

        System.out.println(basicData);


        // 2. 인스턴스에서 찾기
        BasicData basicData1 = new BasicData();
        System.out.println(basicData1.getClass());

        // 3.글자로 찾기
        String className = "org.reflection.data.BasicData";
        Class<?> basicData3 = Class.forName(className);
        System.out.println(basicData3);



    }
}
