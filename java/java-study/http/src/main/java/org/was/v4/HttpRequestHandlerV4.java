package org.was.v4;

import org.was.httpserver.HttpRequest;
import org.was.httpserver.HttpResponse;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;

public class HttpRequestHandlerV4 implements Runnable {
    private final Socket socket;

    public HttpRequestHandlerV4(Socket socket) {
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

            HttpRequest request = new HttpRequest(reader);
            HttpResponse response = new HttpResponse(writer);

            if (request.getPath().equals("/favicon.ico")) {
                System.out.println("favicon요청");
                return;
            }

            System.out.println("http 요청: " + request);

            if (request.getPath().equals("/site1")) {
                site1(response);
            } else if (request.getPath().equals("/site2")) {
                site2(response);
            } else if (request.getPath().equals("/search")) {
                search(request, response);
            } else if (request.getPath().equals("/")) {
                home(response);
            } else {
                notFound(response);
            }

            response.flush();
            System.out.println("응답 완료");
        }

    }

    private void home(HttpResponse response) {
        response.writerBody("<h1>home</h1>");
        response.writerBody("<ul>");
        response.writerBody("<li><a href='/site1'>site1</li>");
        response.writerBody("<li><a href='/site2'>site2</li>");
        response.writerBody("<li><a href='/search?q=hello'>search</li>");
        response.writerBody("</ul>");
        System.out.println("home 응답");
    }

    private void search(HttpRequest request, HttpResponse response) {
        String query = request.getParameter("q");
        response.writerBody("<h1>Search query: " + query + "</h1>");
        System.out.println("search 응답");
    }

    private void site2(HttpResponse response) {
        response.writerBody("<h1> site2222 </h1>");
        System.out.println("site2 응답");
    }

    private void site1(HttpResponse response) {
        response.writerBody("<h1> site1111 </h1>");
        System.out.println("site1 응답");
    }

    private void notFound(HttpResponse response) {
        response.setStatusCode(404);
        response.writerBody("<h1> not found </h1>");
        System.out.println("notfound 응답");

    }

}