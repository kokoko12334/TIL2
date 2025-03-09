package org.reflection;

import org.reflection.data.Team;
import org.reflection.data.User;

public class FieldV3 {
    public static void main(String[] args) {
        User user = new User("id1", null, null);
        Team team = new Team("team1", null);

        System.out.println(user);
        System.out.println(team);
    }
}
