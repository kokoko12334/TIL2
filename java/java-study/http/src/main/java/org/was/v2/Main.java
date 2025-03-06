package org.was.v2;

import java.io.IOException;

public class Main {

    private static final int PORT = 5000;

    public static void main(String[] args) throws IOException {

        HttpServerV2 server = new HttpServerV2(PORT);
        server.start();

    }
}
