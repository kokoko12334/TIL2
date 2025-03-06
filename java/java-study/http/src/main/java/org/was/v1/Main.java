package org.was.v1;

import java.io.IOException;

public class Main {

    private static final int PORT = 5000;

    public static void main(String[] args) throws IOException {
        HttpServerV1 httpServerV1 = new HttpServerV1(PORT);

        httpServerV1.start();
    }
}
