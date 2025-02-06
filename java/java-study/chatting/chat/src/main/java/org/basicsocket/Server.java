package org.basicsocket;

import org.logger.MyLogger;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

import static org.logger.MyLogger.*;

public class Server {
    private static final int PORT = 12345;

    public static void main(String[] args) throws IOException {

        ServerSocket serverSocket = new ServerSocket(PORT);
        log("server start, port: " + PORT);

        while (true) {
            Socket socket = serverSocket.accept();
            SessionManager sessionManager = new SessionManager(socket);
            Thread thread = new Thread(sessionManager);
            thread.start();
        }
        
    }
}
