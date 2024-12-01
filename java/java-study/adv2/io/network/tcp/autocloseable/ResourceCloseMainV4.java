package adv2.io.network.tcp.autocloseable;

public class ResourceCloseMainV4 {

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

        try (ResourceV2 r1 = new ResourceV2("r1");
            ResourceV2 r2 = new ResourceV2("r2")) {

            r1.call();
            r2.callEx();
        } catch (CallException e) {
            System.out.println("ex: " + e);
            throw e;
        }

    }

}
