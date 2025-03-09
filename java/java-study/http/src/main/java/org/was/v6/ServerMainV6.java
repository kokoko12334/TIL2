package org.was.v6;

import org.was.httpserver.HttpServer;
import org.was.httpserver.ServletManager;
import org.was.httpserver.servlet.DiscardServlet;
import org.was.httpserver.servlet.reflection.ReflectionServlet;
import org.was.v5.servlet.HomeServlet;

import java.io.IOException;
import java.util.List;

public class ServerMainV6 {

    private static final int PORT = 12345;

    public static void main(String[] args) throws IOException {
        List<Object> controllers = List.of(new SiteControllerV6(), new SearchControllerV6());
        ReflectionServlet reflectionServlet = new ReflectionServlet(controllers);

        ServletManager servletManager = new ServletManager();
        servletManager.setDefaultServlet(reflectionServlet);
        servletManager.add("/", new HomeServlet());
        servletManager.add("/favicon.ico", new DiscardServlet());

        HttpServer httpServer = new HttpServer(PORT, servletManager);
        httpServer.start();

    }
}
