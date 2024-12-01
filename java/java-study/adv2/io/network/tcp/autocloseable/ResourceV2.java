package adv2.io.network.tcp.autocloseable;

public class ResourceV2 implements AutoCloseable{

    private String name;

    public ResourceV2(String name) {
        this.name = name;
    }

    public void call() {
        System.out.println(name + " call");
    }

    public void callEx() throws CallException {
        System.out.println(name + "callEx");
        throw new CallException(name + "ex");
    }

    @Override // AUtocloseable을 상속하면 close 알아서 호출 with이랑 같은 이치
    public void close() throws CloseException {
        System.out.println(name + " close");
        throw new CloseException(name + "ex");
    }

}
