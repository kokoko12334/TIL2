package org.reflection;

import org.reflection.data.User;

import java.lang.reflect.Field;

public class FieldV2 {
    public static void main(String[] args) throws NoSuchFieldException, IllegalAccessException {
        User user = new User("id1", "userA", "20");
        System.out.println(user);

        Class<? extends User> aClass = user.getClass();

        Field nameField = aClass.getDeclaredField("name");

        // private 허용
        nameField.setAccessible(true);
        nameField.set(user, "userB");
        System.out.println(user);

    }
}
