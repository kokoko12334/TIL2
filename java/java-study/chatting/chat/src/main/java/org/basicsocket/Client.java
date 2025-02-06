package org.basicsocket;

import org.logger.MyLogger;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

import static org.logger.MyLogger.*;

public class Client {

    private static final int PORT = 12345;

    public static void main(String[] args) throws IOException {
        log("client start");
        Socket socket = new Socket("localhost", PORT); // 소켓에 연결요청 -> 서버에서는 backlogue큐에 할당 서버에서 accept를 해주어야 진정한 연결
        DataInputStream input = new DataInputStream(socket.getInputStream());
        DataOutputStream output = new DataOutputStream(socket.getOutputStream());
        log("socket connected: " + socket);

        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.print("메시지를 입력해라: ");
            String msg = sc.nextLine();
            output.writeUTF(msg);

            String response = input.readUTF();
            if (response.equals("exit")) {
                break;
            }
            System.out.println(response);

        }

        log("연결 종료:" + socket);
        output.close();
        input.close();
        socket.close();


    }
}
