package adv2.io.util;

import adv2.was.v1.HttpServerV1;

import java.io.IOException;

public class ServerMain {

    private static final int PORT = 1234;

    public static void main(String[] args) throws IOException {
        HttpServerV1 httpServerV1 = new HttpServerV1(PORT);
        httpServerV1.start();
    }
}
