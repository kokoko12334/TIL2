package org.was.v7;

import org.was.httpserver.HttpRequest;
import org.was.httpserver.HttpResponse;
import org.was.httpserver.servlet.annotation.Mapping;

public class SearchControllerV7 {

    @Mapping("/search")
    public void search(HttpRequest request, HttpResponse response) {
        String query = request.getParameter("q");
        response.writerBody("<h1>Search query: " + query + "</h1>");
        System.out.println("search 응답");
    }
}
