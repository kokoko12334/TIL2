package org.was.v7;

import org.was.httpserver.HttpRequest;
import org.was.httpserver.HttpResponse;
import org.was.httpserver.servlet.annotation.Mapping;

public class SiteControllerV7 {

    @Mapping("/")
    public void service(HttpRequest request, HttpResponse response) {
        response.writerBody("<h1>home</h1>");
        response.writerBody("<ul>");
        response.writerBody("<li><a href='/site1'>site1</li>");
        response.writerBody("<li><a href='/site2'>site2</li>");
        response.writerBody("<li><a href='/search?q=hello'>search</li>");
        response.writerBody("</ul>");
        System.out.println("home 응답");
    }

    @Mapping("/site1")
    public void site1(HttpRequest request, HttpResponse response) {
        response.writerBody("<h1> site1111 </h1>");
        System.out.println("site1 응답");

    }

    @Mapping("/site2")
    public void site2(HttpRequest request, HttpResponse response) {
        response.writerBody("<h1> site2222 </h1>");
        System.out.println("site2 응답");

    }
}
