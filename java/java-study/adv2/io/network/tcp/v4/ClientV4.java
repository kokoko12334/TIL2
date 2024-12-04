package adv2.io.network.tcp.v4;

import adv2.io.network.tcp.SocketCloseUtil;
import adv2.io.util.MyLogger;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

import static adv2.io.network.tcp.SocketCloseUtil.*;
import static adv2.io.util.MyLogger.log;

public class ClientV4 {

    private static final int PORT = 12345;

    public static void main(String[] args) throws IOException {

        Socket socket = null;
        DataInputStream input = null;
        DataOutputStream output = null;
        try {
            log("클라이언트 시작");
            socket = new Socket("localhost", PORT);

            input = new DataInputStream(socket.getInputStream());
            output = new DataOutputStream(socket.getOutputStream());
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

        } catch (IOException e) {
            MyLogger.log(e);
        } finally {
            closeAll(socket, input, output);
            log("연결 종료:" + socket);
        }
    }
}
