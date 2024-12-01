package adv2.io.network.tcp.autocloseable;

public class ResourceCloseMainV3 {

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

        try {
            r1.call();
            r2.callEx();
        } catch (CallException e) {
            System.out.println("ex : " + e);
            throw e;
        } finally {
            System.out.println("자원정리");

            try {
                r2.closeEx();
            } catch (CloseException e) {
                System.out.println("클로즈익셉션:" + e);
            }

            try {
                r1.closeEx();
            } catch (CloseException e) {
                System.out.println("클로즈익셉션:" + e);
            }

        }
    }
}
