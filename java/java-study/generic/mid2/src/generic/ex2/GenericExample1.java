package generic.ex2;

public class GenericExample1<T extends Number> {
    private final T number;

    public GenericExample1(T number) {
        this.number = number;
    }

    public T getNumber() {
        return number;
    }
}
