package org.reflection.data;

public class BasicData {

    public String publicFiled;
    private int privateFiled;

    public BasicData() {
        System.out.println("BasicData.BasicData");
    }

    private BasicData(String data) {
        System.out.println("BasicData.BasicData: " + data);
    }

    public void call() {
        System.out.println("BasicData.call");
    }

    public String hello(String str) {
        return str + "hello";
    }

    private void privateMethod() {
        System.out.println("privatemethod");
    }

    void defaultMethod() {
        System.out.println("defaultMethod");
    }

    protected void protectedmethod() {
        System.out.println("protectedMethod");
    }

}
