package generic.ex2;

import java.util.ArrayList;
import java.util.List;

public class Main2 {
    public static void main(String[] args) {

        List<Number> numList = new ArrayList<>();
        AddToList.addToList(numList);
        System.out.println(numList.get(0));// List<Number>에 Integer 추가

        List<Object> objList = new ArrayList<>();
        AddToList.addToList(objList); // List<Object>에 Integer 추가
    }
}