package generic.ex1;

public class BoxMain3 {
    public static void main(String[] args) {

        GenericBox<Integer> integerBox = new GenericBox<Integer>(); // 생성시점에 즉 런타임에 동적
        integerBox.setValue(10);
        Integer num = integerBox.getValue();
        System.out.println(num);
    }
}
