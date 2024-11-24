package generic.ex2;

import java.util.ArrayList;
import java.util.List;

public class AddToList {
    public static void addToList(List<? super Integer> list) {
        list.add(10); // Integer를 추가할 수 있음
    }

}