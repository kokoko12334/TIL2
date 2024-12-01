package adv2.io.network.tcp.v3;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

import static adv2.io.util.MyLogger.log;

public class ClientV3 {

    private static final int PORT = 12345;

    public static void main(String[] args) throws IOException {
        log("클라이언트 시작");
        Socket socket = new Socket("localhost", PORT);

        DataInputStream input = new DataInputStream(socket.getInputStream());
        DataOutputStream output = new DataOutputStream(socket.getOutputStream());
        log("소켓 연결: " + socket);

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("전송문자: ");
            String toSend = scanner.nextLine();

            output.writeUTF(toSend);
            log("client -> server: " + toSend);

            if (toSend.equals("exit")) {
                break;
            }
            String received = input.readUTF();
            log("client <- server: " + received);

        }

        log("연결 종료:" + socket);
        input.close();
        output.close();
        socket.close();
    }
}