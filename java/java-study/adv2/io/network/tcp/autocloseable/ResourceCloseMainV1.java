package adv2.io.network.tcp.autocloseable;

public class ResourceCloseMainV1 {

    public static void main(String[] args) {
        try {
            logic();
        } catch (CallException e) {
            System.out.println("call error");
            throw new RuntimeException(e);
        } catch (CloseException e) {
            System.out.println("close error");
            throw new RuntimeException(e);

        }
    }

    private static void logic() throws CallException, CloseException {
        ResourceV1 r1 = new ResourceV1("r1");
        ResourceV1 r2 = new ResourceV1("r2");

        r1.call();
        r2.callEx();

        System.out.println("자원정리");
        r1.closeEx();
        r2.closeEx();

    }
}
