package org.was.httpserver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

public class HttpRequestHandler implements Runnable {
    private final Socket socket;
    private final ServletManager servletManager;

    public HttpRequestHandler(Socket socket, ServletManager servletManager) {
        this.socket = socket;
        this.servletManager = servletManager;
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

            System.out.println("http 요청: " + request);
            servletManager.execute(request, response);

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