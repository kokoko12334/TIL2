package org.was.httpserver.servlet.annotation;

import org.was.httpserver.HttpRequest;
import org.was.httpserver.HttpResponse;
import org.was.httpserver.HttpServlet;
import org.was.httpserver.PageNotFoubdException;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.List;

public class AnnotationServletV1 implements HttpServlet {

    private final List<Object> controllers;

    public AnnotationServletV1(List<Object> controllers) {
        this.controllers = controllers;
    }

    @Override
    public void service(HttpRequest request, HttpResponse response) throws IOException, InvocationTargetException, IllegalAccessException {
        String path = request.getPath();

        for (Object controller: controllers) {
            Method[] declaredMethods = controller.getClass().getDeclaredMethods();
            for (Method method: declaredMethods) {
                Mapping annotation = method.getAnnotation(Mapping.class);
                String value = annotation.value();
                if (value.equals(path)) {
                    method.invoke(controller, request, response);
                    return;
                }
            }
        }

        throw new PageNotFoubdException("페이지 없음");
    }
}
