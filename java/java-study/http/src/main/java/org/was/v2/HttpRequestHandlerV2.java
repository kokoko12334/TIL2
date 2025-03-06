package org.was.v2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

public class HttpRequestHandlerV2 implements Runnable {
    private final Socket socket;

    public HttpRequestHandlerV2(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
        try {
            process();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void process() throws IOException {
        try(socket;
            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), false, StandardCharsets.UTF_8);
        ) {
            String requestString = requestToString(reader);
            if (requestString.contains("/favicon.ico")) {
                System.out.println("favicon요청");
                return;
            }

            System.out.println("http 요청: " + requestString);
//            try {
//                Thread.sleep(5000);
//            } catch (InterruptedException e) {
//                throw new RuntimeException(e);
//            }

            responseToClient(writer);

            System.out.println("요청 완료");
        }

    }

    private void responseToClient(PrintWriter writer) {
        String body = "<h1> Hello </h1>";
        int length = body.getBytes(StandardCharsets.UTF_8).length;

        StringBuilder sb = new StringBuilder();
        sb.append("HTTP/1.1 300 ok\r\n");
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

    private String requestToString(BufferedReader reader) throws IOException {

        StringBuilder sb = new StringBuilder();
        String line;
        while((line = reader.readLine()) != null) {
            if (line.isEmpty()) {
                break;
            }
            sb.append(line).append("\r\n");
        }
        return sb.toString();
    }
}
