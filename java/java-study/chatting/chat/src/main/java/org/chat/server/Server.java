package org.chat.server;

public class Server {

    private final int port;
    private final CommandManager commandManager;

    public Server(int port, CommandManager commandManager) {
        this.port = port;
        this.commandManager = commandManager;
    }
}
