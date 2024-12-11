package adv2;

public class Main {
    public static void main(String[] args) {

        int x = 1;
        int sum = 0;
        for (int i=0; i< 4; i++) {
            x++;
            sum += increment();

        }
        System.out.printf("합: %d", sum);
    }

    private static int increment() {
        int x = 0;
        x += 2;
        return x;
    }
}
