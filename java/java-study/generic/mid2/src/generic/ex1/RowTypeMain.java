package generic.ex1;

public class RowTypeMain {
    public static void main(String[] args) {
        GenericBox integerBox = new GenericBox(); // <>를 안쓰면 Object로 지정됨.
        integerBox.setValue(1333);
        Integer num = (Integer) integerBox.getValue();
        System.out.println(num);
    }
}
