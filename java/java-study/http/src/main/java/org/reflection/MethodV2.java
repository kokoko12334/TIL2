package org.reflection;

import org.reflection.data.BasicData;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class MethodV2 {
    public static void main(String[] args) throws ClassNotFoundException, NoSuchMethodException, InvocationTargetException, IllegalAccessException {

        // 동적으로 메소드 호출
        BasicData basicData = new BasicData();

        Class<?> basicDataClass = basicData.getClass();
        
        String methodName = "hello"; // 이부분에서 동적으로 수정가능
        
        //메소드이름, 매개인자 타입
        Method method1 = basicDataClass.getDeclaredMethod(methodName, String.class); //패지키/클래스, 메소드 이름만 안 상태
        System.out.println(method1.invoke(basicData, "good"));


        Method method2 = basicDataClass.getDeclaredMethod("privateMethod");
        method2.setAccessible(true);
        method2.invoke(basicData);

    }
}
