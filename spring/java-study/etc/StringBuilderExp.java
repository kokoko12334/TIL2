package etc;

public class StringBuilderExp {

    public static void main(String[] args) {
        // 테스트 반복 횟수
        int iterations = 100000;

        // String을 사용한 문자열 결합
        long startTime = System.nanoTime();
        String str = "";
        for (int i = 0; i < iterations; i++) {
            str = str + "a";  // 새로운 String 객체가 매번 생성됨
        }
        long endTime = System.nanoTime();
        double stringTime = (endTime - startTime) / 1_000_000_000.0;
        System.out.println("String을 사용한 결합 시간: " + stringTime + "s");

        // StringBuilder를 사용한 문자열 결합
        startTime = System.nanoTime();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < iterations; i++) {
            sb.append("a");  // 내부 버퍼를 수정
        }
        endTime = System.nanoTime();
        double stringBuilderTime = (endTime - startTime) / 1_000_000_000.0;
        System.out.println("StringBuilder를 사용한 결합 시간: " + stringBuilderTime + "s");
    }
}
