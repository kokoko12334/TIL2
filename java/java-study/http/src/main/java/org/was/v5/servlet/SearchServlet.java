package org.was.v5.servlet;

import org.was.httpserver.HttpRequest;
import org.was.httpserver.HttpResponse;
import org.was.httpserver.HttpServlet;

import java.io.IOException;

public class SearchServlet implements HttpServlet {
    @Override
    public void service(HttpRequest request, HttpResponse response) {
        String query = request.getParameter("q");
        response.writerBody("<h1>Search query: " + query + "</h1>");
        System.out.println("search 응답");
    }
}
