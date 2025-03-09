package org.was.v6;

import org.was.httpserver.HttpRequest;
import org.was.httpserver.HttpResponse;

public class SiteControllerV6 {

    public void site1(HttpRequest request, HttpResponse response) {
        response.writerBody("<h1> site1111 </h1>");
        System.out.println("site1 응답");

    }

    public void site2(HttpRequest request, HttpResponse response) {
        response.writerBody("<h1> site2222 </h1>");
        System.out.println("site2 응답");

    }
}
