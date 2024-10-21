

public class Test {

    public static void main(String[] args) {
        class Person {
            private String name; // 인스턴스 변수

            public Person(String val) { // 매개변수 이름도 name
                name = val; // 여기서 인스턴스 변수에 값을 할당하지 않음
            }

            public String getName() {
                return name; // 인스턴스 변수는 초기화되지 않음
            }
        }

// 사용 예시
        Person person = new Person("Alice");
        System.out.println(person.getName()); // null 출력
    }
}
