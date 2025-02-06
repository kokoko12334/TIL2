package org.basicsocket;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

import static org.logger.MyLogger.*;

public class Server123 {
    private static final int PORT = 12345;

    public static void main(String[] args) throws IOException {

        ServerSocket serverSocket = new ServerSocket(PORT);
        log("server start, port: " + PORT);

        while (true) {
            Socket socket = serverSocket.accept();
            SessionManager123 sessionManager123 = new SessionManager123(socket);
            Thread thread = new Thread(sessionManager123);
            thread.start();
        }

    }
}
