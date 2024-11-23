import java.util.EnumSet;

public class Main {
    public static void main(String[] args) {

        enum Day {
            MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
        }

        // EnumSet을 사용하여 주말을 포함하는 Set 생성
        EnumSet<Day> weekend = EnumSet.of(Day.SATURDAY, Day.SUNDAY);
        System.out.println("Weekend days: " + weekend);
    }
}
