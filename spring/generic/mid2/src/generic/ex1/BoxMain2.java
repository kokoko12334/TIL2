package generic.ex1;

public class BoxMain2 {
    public static void main(String[] args) {

        ObjectBox objectBox = new ObjectBox();
        objectBox.setValue(10);
        Object object = objectBox.getValue();
        Integer integer = (Integer) object;
        System.out.println(integer);


        objectBox.setValue("ddd");
    }
}
