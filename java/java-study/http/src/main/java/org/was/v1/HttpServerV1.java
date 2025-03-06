package org.was.v1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

public class HttpServerV1 {

    private final int port;

    public HttpServerV1(int port) {
        this.port = port;
    }


    public void start() throws IOException {
        ServerSocket serverSocket = new ServerSocket(port);
        System.out.println("서버 시작: " + port);

        while (true) {
            Socket socket = serverSocket.accept();
            process(socket);
        }

    }

    private void process(Socket socket) throws IOException {

        try (socket;
             BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));
             PrintWriter writer = new PrintWriter(socket.getOutputStream(), false, StandardCharsets.UTF_8);
        ) {
            String requestString = requestToString(reader);

            if (requestString.contains("/favicon.ico")) {
                System.out.println("favicon요청");
                return;
            }

            System.out.println("http요청: " + requestString);

            System.out.println("http 응답 생성 중");
//            try {
//                Thread.sleep(3000);
//            } catch (InterruptedException e) {
//                throw new RuntimeException(e);
//            }
            responseToClinet(writer);

        }

    }

    private void responseToClinet(PrintWriter writer) {

        String body = "<h1> Hello </h1>";
        int length = body.getBytes(StandardCharsets.UTF_8).length;

        StringBuilder sb = new StringBuilder();
        sb.append("HTTP/1.1 200 ok\r\n");
        sb.append("Content-Type: text/html\r\n");
        sb.append("Content-Length: ").append(length).append("\r\n");
        sb.append("\r\n");
        sb.append(body);

        System.out.println("HTTP 응답 정보 출력");
        System.out.println(sb);

        writer.println(sb);
        writer.flush();
        System.out.println("HTTP 응답 정보 전달 완료");

    }

    private static String requestToString(BufferedReader reader) throws IOException {
        StringBuilder sb = new StringBuilder();
        String line;

        while ((line = reader.readLine()) != null) {
            if (line.isEmpty()) {
                break;
            }
            sb.append(line).append("\n");

        }
        return sb.toString();
    }

}
