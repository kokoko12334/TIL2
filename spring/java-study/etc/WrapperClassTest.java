package etc;

public class WrapperClassTest {
    private static int counter = 0;

    public static void main(String[] args) {
        int iter = 10000;
        Runnable task = () -> {
            for (int i = 0; i < iter; i++) {
                counter++;  // 동시성 문제 발생 가능
            }
        };

        Runnable task2 = () -> {
            for (int i = 0; i < iter; i++) {
                counter--;  // 동시성 문제 발생 가능
            }
        };

        // 2개의 스레드 생성
        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task2);
        t1.start();
        t2.start();

        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("counter = " + counter);  // 예상과 다를 수 있음
    }
}
