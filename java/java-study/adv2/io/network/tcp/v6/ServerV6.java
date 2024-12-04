package adv2.io.network.tcp.v6;


import adv2.io.network.tcp.v5.SessionV5;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

import static adv2.io.util.MyLogger.log;

public class ServerV6 {

    private static final int PORT = 12345;

    public static void main(String[] args) throws IOException {
        log("서버 시작");
        SessionManagerV6 sessionManager = new SessionManagerV6();
        ServerSocket serverSocket = new ServerSocket(PORT);
        log("서버 소켓 시작- 리스닝 포트" + PORT);

        //셧다운 등록

        ShutdownHook shutdownHook = new ShutdownHook(serverSocket, sessionManager);
        Runtime.getRuntime().addShutdownHook(new Thread(shutdownHook, "shutdown hook-all-resources closed"));

        try {
            while (true) {
                Socket socket = serverSocket.accept();
                log("소켓 연결: " + socket);

                SessionV6 session = new SessionV6(socket, sessionManager);
                Thread thread = new Thread(session);
                thread.start();
            }

        } catch (IOException e) {
            log("소켓 종류" + e);
        }

    }

    //자바에서 **셧다운 훅(Shutdown Hook)**은 JVM(Java Virtual Machine) 종료 시, 특정 작업을 자동으로 실행하도록 설정할 수 있는 메커니즘입니다.
    static class ShutdownHook implements Runnable {
        private final ServerSocket serverSocket;
        private final SessionManagerV6 sessionManager;

        ShutdownHook(ServerSocket serverSocket, SessionManagerV6 sessionManager) {
            this.serverSocket = serverSocket;
            this.sessionManager = sessionManager;
        }


        @Override
        public void run() {
            log("shutdown hook 실행");
            sessionManager.closeAll();
            try {
                serverSocket.close();
                Thread.sleep(1000); // 자원정리 대기
            } catch (Exception e) {
                e.printStackTrace();
                System.out.println("e = " + e);
            }
        }
    }

}
