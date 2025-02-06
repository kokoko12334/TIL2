package org.chat.client;

import org.logger.MyLogger;

import java.io.DataOutputStream;
import java.io.IOException;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class WriteHandler implements Runnable{

    private static final String DELIMITER = "|";

    private final DataOutputStream output;
    private final Client client;

    private boolean closed = false;

    public WriteHandler(DataOutputStream output, Client client) {
        this.output = output;
        this.client = client;
    }

    @Override
    public void run() {

        Scanner sc = new Scanner(System.in);

        try {
            String username = inputUsername(sc);
            output.writeUTF("/join" + DELIMITER + username);

            while (true) {
                String toSend = sc.nextLine();
                if (toSend.isEmpty()) {
                    continue;
                }

                if (toSend.equals("/exit")) {
                    output.writeUTF(toSend);
                    break;
                }

                // "/"로 시작하면 명령어, 나머지는 일반 메시지
                if (toSend.startsWith("/")) {
                    output.writeUTF(toSend);
                } else {
                    output.writeUTF("/message" + DELIMITER + toSend);
                }

            }

        } catch (IOException | NoSuchElementException e) {
            MyLogger.log(e);
        } finally {
            try {
                client.close();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }

    private static String inputUsername(Scanner sc) {
        System.out.println("이름을 입력하세요.");
        String username;
        do {
            username = sc.nextLine();
        } while (username.isEmpty());
        return username;
    }

    public synchronized void close() {
        if (closed) {
            return;
        }

        try {
            System.in.close(); // 사용자의 입력을 닫음.
        } catch (IOException e) {
            MyLogger.log(e);
        }
        closed = true;
        MyLogger.log("writehandler 종료");

    }
}
