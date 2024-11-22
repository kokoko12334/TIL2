public class TestMain {


    public static void main(String[] args) {
        Day today = Day.MONDAY;

        switch (today) {
            case Day.MONDAY:
                System.out.println("Start of the work week.");
                break;
            case Day.FRIDAY:
                System.out.println("It's almost the weekend!");
                break;
            case Day.SATURDAY:
            case Day.SUNDAY:
                System.out.println("It's the weekend. Relax!");
                break;
            default:
                System.out.println("Midweek hustle.");
        }
    }

}

