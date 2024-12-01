package adv2.io.network.tcp.v3;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

import static adv2.io.util.MyLogger.log;

public class SessionV3  implements Runnable{
    private final Socket socket;

    public SessionV3(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {

        try {
            DataInputStream input = new DataInputStream(socket.getInputStream());
            DataOutputStream output = new DataOutputStream(socket.getOutputStream());

            while (true) {
                String received = input.readUTF(); //블락킹
                log("client -> server: " + received);

                if (received.equals("exit")) {
                    break;
                }

                String toSend = received + "WORLD";
                output.writeUTF(toSend);

            }
            log("연결 종료: " + socket);
            input.close();
            output.close();
            socket.close();

        } catch (IOException e ) {
            throw new RuntimeException(e);
        }



    }

}
