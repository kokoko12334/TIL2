package generic.ex1;

public class SwapMain {
    public static void main(String[] args) {

//        int[] intArray = {1, 2, 3, 4};
//        System.out.println("교환 전: " + java.util.Arrays.toString(intArray));
//        SwapUtil.swap(intArray, 0, 2); // 첫 번째와 세 번째 요소 교환
//        System.out.println("교환 후: " + java.util.Arrays.toString(intArray));
//
//        // double 배열 예제
//        double[] doubleArray = {1.1, 2.2, 3.3};
//        System.out.println("교환 전: " + java.util.Arrays.toString(doubleArray));
//        SwapUtil.swap(doubleArray, 0, 1); // 첫 번째와 두 번째 요소 교환
//        System.out.println("교환 후: " + java.util.Arrays.toString(doubleArray));
//
//        // String 배열 예제
//        String[] strArray = {"apple", "banana", "cherry"};
//        System.out.println("교환 전: " + java.util.Arrays.toString(strArray));
//        SwapUtil.swap(strArray, 1, 2); // 두 번째와 세 번째 요소 교환
//        System.out.println("교환 후: " + java.util.Arrays.toString(strArray));

        // Integer 타입 배열
        Integer[] intArray = {1, 2, 3, 4};
        GenericSwapUtil.swap(intArray, 0, 1); // Integer 타입 배열

        // String 타입 배열
        String[] strArray = {"apple", "banana", "cherry"};
        GenericSwapUtil.swap(strArray, 0, 1); // String 타입 배열
    }
}
