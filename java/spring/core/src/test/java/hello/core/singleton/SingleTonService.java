package hello.core.singleton;

public class SingleTonService {

    private static SingleTonService instance = null;

    private SingleTonService() {
    }

    public static SingleTonService getInstance() {
        if (instance == null) {
            instance = new SingleTonService();
        }
        return instance;
    }

    public static void main(String[] args) {
        SingleTonService instance1 = SingleTonService.getInstance();
        SingleTonService instance2 = SingleTonService.getInstance();
        SingleTonService instance3 = SingleTonService.getInstance();

        System.out.println(instance1);
        System.out.println(instance2);
        System.out.println(instance3);
    }
}
