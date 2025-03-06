package org.was.v3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;

public class HttpRequestHandlerV3 implements Runnable {
    private final Socket socket;

    public HttpRequestHandlerV3(Socket socket) {
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

            if (requestString.startsWith("GET /site1")) {
                site1(writer);
            } else if (requestString.startsWith("GET /site2")) {
                site2(writer);
            } else if (requestString.startsWith("GET /search")) {
                search(writer, requestString);
            } else if (requestString.startsWith("GET / ")) {
                home(writer);
            } else {
                notFound(writer);
            }

            System.out.println("응답 완료");
        }

    }

    private void notFound(PrintWriter writer) {
        writer.println("HTTP/1.1 404 Not Found");
        writer.println("Content-Type: text/html, charset=UTF-8");
        writer.println();
        writer.println("<h1> not found </h1>");
        writer.flush();
        System.out.println("notfound 응답");

    }

    private void home(PrintWriter writer) {
        writer.println("HTTP/1.1 200 OK");
        writer.println("Content-Type: text/html, charset=UTF-8");
        writer.println();
        writer.println("<h1>home</h1>");
        writer.println("<ul>");
        writer.println("<li><a href='/site1'>site1</li>");
        writer.println("<li><a href='/site2'>site2</li>");
        writer.println("<li><a href='/search?q=hello'>search</li>");
        writer.println("</ul>");
        writer.flush();
        System.out.println("home 응답");
    }

    private void search(PrintWriter writer, String requestString) {
        int startIndex = requestString.indexOf("q=");
        int endIndex = requestString.indexOf(" ", startIndex + 2);

        System.out.println("end: " + endIndex);

        String query = requestString.substring(startIndex + 2, endIndex);
        String decode = URLDecoder.decode(query, StandardCharsets.UTF_8);

        writer.println("HTTP/1.1 200 OK");
        writer.println("Content-Type: text/html, charset=UTF-8");
        writer.println();
        writer.println("<h1>Search query: " + query + "</h1>");

        writer.println("<h1>Search decode: " + decode + "</h1>");
        writer.flush();

    }

    private void site2(PrintWriter writer) {
        writer.println("HTTP/1.1 200 OK");
        writer.println("Content-Type: text/html, charset=UTF-8");
        writer.println();
        writer.println("<h1> site2222 </h1>");
        writer.flush();
        System.out.println("site2 응답");

    }

    private void site1(PrintWriter writer) {
        writer.println("HTTP/1.1 200 OK");
        writer.println("Content-Type: text/html, charset=UTF-8");
        writer.println();
        writer.println("<h1> site1111 </h1>");
        writer.flush();
        System.out.println("site1 응답");
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
