package org.was.v7;

import org.was.httpserver.HttpServer;
import org.was.httpserver.HttpServlet;
import org.was.httpserver.ServletManager;
import org.was.httpserver.servlet.DiscardServlet;
import org.was.httpserver.servlet.annotation.AnnotationServletV1;

import java.io.IOException;
import java.util.List;

public class Main {

    private static final int PORT = 1235;

    public static void main(String[] args) throws IOException {
        List<Object> objects = List.of(new SiteControllerV7(), new SearchControllerV7());

        AnnotationServletV1 annotationServletV1 = new AnnotationServletV1(objects);

        ServletManager servletManager = new ServletManager();
        servletManager.setDefaultServlet(annotationServletV1);
        servletManager.add("/favicon.ico", new DiscardServlet());

        HttpServer httpServer = new HttpServer(PORT, servletManager);
        httpServer.start();

    }
}
