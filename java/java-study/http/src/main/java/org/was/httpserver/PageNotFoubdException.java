package org.was.httpserver;

public class PageNotFoubdException extends RuntimeException {
    public PageNotFoubdException(String message) {
        super(message);
    }
}
