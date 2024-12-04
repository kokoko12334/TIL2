package adv2.io.network.tcp.v6;

import adv2.io.network.tcp.SocketCloseUtil;
import adv2.io.util.MyLogger;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

import static adv2.io.util.MyLogger.log;

public class SessionV6 implements Runnable {
    private final Socket socket;
    private final DataInputStream input;
    private final DataOutputStream output;
    private final SessionManagerV6 sessionManager;
    private boolean closed = false;

    public SessionV6(Socket socket, SessionManagerV6 sessionManager) throws IOException {
        this.socket = socket;
        this.input = new DataInputStream(socket.getInputStream());
        this.output = new DataOutputStream(socket.getOutputStream());
        this.sessionManager = sessionManager;
        this.sessionManager.add(this);
    }

    @Override
    public void run() {

        try {
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
        } finally {
            sessionManager.remove(this);
            close();
        }
    }

    public synchronized void close() {

        if (closed) {
            return;
        }

        SocketCloseUtil.closeAll(socket, input, output);
        closed = true;
        log("연결종료:" + socket.isClosed());
    }

}
