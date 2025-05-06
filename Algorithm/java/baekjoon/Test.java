public class Test {

    public static void main(String[] args) {


        String a = "a";
        String b = a + "b".repeat(100000000);
        String c = b + "c";


        long start = System.currentTimeMillis();

        c.contains("a");
        long end = System.currentTimeMillis();
        System.out.println("실행 시간: " + (end -start) + "ms");


        long start2 = System.currentTimeMillis();
        c.contains("c");
        long end2 = System.currentTimeMillis();
        System.out.println("실행 시간: " + (end2 -start2) + "ms");


    }
}
