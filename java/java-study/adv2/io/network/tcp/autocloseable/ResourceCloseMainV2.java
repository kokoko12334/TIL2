package adv2.io.network.tcp.autocloseable;

public class ResourceCloseMainV2 {

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
            r1.closeEx(); // finally해도 닫는 과정에서도 exception 발생함. 그 뒤에 있는 것은 실행이 안됨.
            r2.closeEx(); // 사실 callex가 메인 예외인데 추가로 closeEx가 터져서 이게 덮여쓰여진다.(출력할때)

        }
    }
}
