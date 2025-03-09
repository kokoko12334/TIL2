package org.was.v6;

import org.was.httpserver.HttpRequest;
import org.was.httpserver.HttpResponse;

public class SearchControllerV6 {

    public void search(HttpRequest request, HttpResponse response) {
        String query = request.getParameter("q");
        response.writerBody("<h1>Search query: " + query + "</h1>");
        System.out.println("search 응답");
    }
}
