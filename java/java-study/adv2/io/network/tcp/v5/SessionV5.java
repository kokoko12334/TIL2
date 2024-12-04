package adv2.io.network.tcp.v5;

import adv2.io.network.tcp.SocketCloseUtil;
import adv2.io.util.MyLogger;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

import static adv2.io.util.MyLogger.log;

public class SessionV5 implements Runnable {
    private final Socket socket;

    public SessionV5(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {

        try (socket;
             DataInputStream input = new DataInputStream(socket.getInputStream());
             DataOutputStream output = new DataOutputStream(socket.getOutputStream());
        ) {

            while (true) {
                String received = input.readUTF(); //블락킹
                log("client -> server: " + received);

                if (received.equals("exit")) {
                    break;
                }

                String toSend = received + "WORLD";
                output.writeUTF(toSend);

            }

        } catch (IOException e) {
            MyLogger.log(e);
        }

        log("연결종료:" + socket.isClosed());
    }

}
