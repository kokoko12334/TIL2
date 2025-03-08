package org.was.v5.servlet;

import org.was.httpserver.HttpRequest;
import org.was.httpserver.HttpResponse;
import org.was.httpserver.HttpServlet;

import java.io.IOException;

public class HomeServlet implements HttpServlet {
    @Override
    public void service(HttpRequest request, HttpResponse response) {
        response.writerBody("<h1>home</h1>");
        response.writerBody("<ul>");
        response.writerBody("<li><a href='/site1'>site1</li>");
        response.writerBody("<li><a href='/site2'>site2</li>");
        response.writerBody("<li><a href='/search?q=hello'>search</li>");
        response.writerBody("</ul>");
        System.out.println("home 응답");
    }
}
