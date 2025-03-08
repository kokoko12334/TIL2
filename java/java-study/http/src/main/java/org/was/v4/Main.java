package org.was.v4;

import java.io.IOException;

public class Main {
    private static final int PORT = 5000;

    public static void main(String[] args) throws IOException {
        HttpServerV4 httpServerV4 = new HttpServerV4(PORT);
        httpServerV4.start();
    }
}
