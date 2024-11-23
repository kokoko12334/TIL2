package generic.ex1;

public class CompareMain {
    public static void main(String[] args) {

        ObjectCompare compare = new ObjectCompare();

        Object a = compare.compare("Ddd", 3);
//        int result = (int) a;
        System.out.println(a);
    }
}
