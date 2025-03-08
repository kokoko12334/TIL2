package org.was.httpserver;

import org.was.v4.HttpRequestHandlerV4;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class HttpServer {
    private final ExecutorService es = Executors.newFixedThreadPool(10);
    private final int port;
    private final ServletManager servletManager;

    public HttpServer(int port, ServletManager servletManager) {
        this.port = port;
        this.servletManager = servletManager;
    }

    public void start() throws IOException {
        ServerSocket serverSocket = new ServerSocket(port);
        System.out.println("서버시작: " + port);
        while (true) {
            Socket socket = serverSocket.accept();
            es.submit(new HttpRequestHandler(socket, servletManager));
        }
    }
}
