package org.was.v3;

import java.io.IOException;

public class Main {
    private static final int PORT = 5000;

    public static void main(String[] args) throws IOException {
        HttpServerV3 httpServerV3 = new HttpServerV3(PORT);

        httpServerV3.start();
    }
}
