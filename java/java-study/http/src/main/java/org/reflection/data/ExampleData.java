package org.reflection.data;

public class ExampleData {

    public String publicFiled;
    private int privateFiled;

    public ExampleData() {
        System.out.println("BasicData.BasicData");
    }

    private ExampleData(String data) {
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
