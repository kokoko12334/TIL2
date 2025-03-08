package org.was.v5;

import org.was.httpserver.HttpServer;
import org.was.httpserver.ServletManager;
import org.was.httpserver.servlet.DiscardServlet;
import org.was.v5.servlet.HomeServlet;
import org.was.v5.servlet.SearchServlet;
import org.was.v5.servlet.Site1Servlet;
import org.was.v5.servlet.Site2Servlet;

import java.io.IOException;

public class Main {
    private static final int PORT = 5000;

    public static void main(String[] args) throws IOException {
        ServletManager servletManager = new ServletManager();
        servletManager.add("/", new HomeServlet());
        servletManager.add("/site1", new Site1Servlet());
        servletManager.add("/site2", new Site2Servlet());
        servletManager.add("/search", new SearchServlet());
        servletManager.add("/favicon.ico", new DiscardServlet());

        HttpServer server = new HttpServer(PORT, servletManager);
        server.start();
    }
}
