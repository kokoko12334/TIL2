package org.was.v5.servlet;

import org.was.httpserver.HttpRequest;
import org.was.httpserver.HttpResponse;
import org.was.httpserver.HttpServlet;

import java.io.IOException;

public class Site2Servlet implements HttpServlet {

    @Override
    public void service(HttpRequest request, HttpResponse response) {
        response.writerBody("<h1> site2222 </h1>");
        System.out.println("site2 응답");
    }
}
