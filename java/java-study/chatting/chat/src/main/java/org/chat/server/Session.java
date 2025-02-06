package org.chat.server;

import org.logger.MyLogger;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class Session implements Runnable{

    private final Socket socket;
    private final DataInputStream input;
    private final DataOutputStream output;

    private final CommandManager commandManager;
    private final SessionManager sessionManager;

    private boolean closed = false;
    private String username;

    public Session(Socket socket, CommandManager commandManager, SessionManager sessionManager) throws IOException {
        this.socket = socket;
        this.input = new DataInputStream(socket.getInputStream());
        this.output = new DataOutputStream(socket.getOutputStream());
        this.commandManager = commandManager;
        this.sessionManager = sessionManager;
        this.sessionManager.add(this);
    }

    @Override
    public void run() {

        try {
            while (true) {
                String res = input.readUTF();
                MyLogger.log("client -> server: " + res);
                commandManager.execute(res, this);
            }

        } catch (IOException e) {
            MyLogger.log(e);
        } finally {
            sessionManager.remove(this);
            sessionManager.sendAll(username + "님이 나감");
            try {
                close();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

    }

    public void send(String message) throws IOException {
        MyLogger.log("server -> clinet: " + message);
        output.writeUTF(message);
    }

    public void close() throws IOException {
        if (closed) {
            return;
        }

        output.close();
        input.close();
        socket.close();
        closed = true;
        MyLogger.log("연결 종료");


    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
}
