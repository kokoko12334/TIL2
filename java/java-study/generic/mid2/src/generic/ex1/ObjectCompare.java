package generic.ex1;

public class ObjectCompare {
    public Object compare(Object a, Object b) {
        if (((Comparable) a).compareTo(b) > 0) {
            return a;
        }
        return b;
    }
}
