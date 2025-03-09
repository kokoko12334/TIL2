package org.was.httpserver.servlet.reflection;

import org.was.httpserver.HttpRequest;
import org.was.httpserver.HttpResponse;
import org.was.httpserver.HttpServlet;
import org.was.httpserver.PageNotFoubdException;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.List;

public class ReflectionServlet implements HttpServlet {

    private final List<Object> controllers;

    public ReflectionServlet(List<Object> controllers) {
        this.controllers = controllers;
    }


    @Override
    public void service(HttpRequest request, HttpResponse response) throws IOException, InvocationTargetException, IllegalAccessException {
        String path = request.getPath();

        for (Object controller: controllers) {
            Class<?> aClass = controller.getClass();
            Method[] methods = aClass.getDeclaredMethods();
            for (Method method: methods) {
                String methodName = method.getName();
                if (path.equals("/" + methodName)) {
                    method.invoke(controller, request, response);
                    return;
                }

            }
        }
        throw new PageNotFoubdException("request = " + path);
    }
}
