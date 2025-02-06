package org.chat.server;

import org.logger.MyLogger;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class SessionManager {

    private List<Session> sessions = new ArrayList<>();

    public synchronized void add(Session session) {
        sessions.add(session);
    }

    public synchronized void remove(Session session) {
        sessions.remove(session);
    }

    public synchronized void closeAll() throws IOException {
        for (Session session: sessions) {
            session.close();
        }
        sessions.clear();

    }

    public void sendAll(String message) {
        for (Session session: sessions) {
            try {
                session.send(message);
            } catch (IOException e) {
                MyLogger.log(e);
            }
        }

    }

    public synchronized List<String> getAllUsername() {
        List<String> usernames = new ArrayList<>();

        for (Session session: sessions) {
            if (session.getUsername() != null) {
                usernames.add(session.getUsername());
            }
        }
        return usernames;
    }
}