package org.chat.client;

import org.logger.MyLogger;

import java.io.DataInputStream;
import java.io.IOException;

public class ReadHandler implements Runnable{

    private final DataInputStream input;
    private final Client client;
    public boolean closed = false;

    public ReadHandler(DataInputStream input, Client client) {
        this.input = input;
        this.client = client;
    }

    @Override
    public void run() {

        while (true) {

            String res = null;
            try {
                res = input.readUTF();
                System.out.println(res);
            } catch (IOException e) {
                MyLogger.log(e);
            } finally {
                try {
                    client.close();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        }

    }

    public synchronized void close() {
        if (closed) {
            return;
        }

        closed = true;
        MyLogger.log("readhandler 종료");

    }
}
