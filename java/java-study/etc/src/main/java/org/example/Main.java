package org.example;


import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        List<String> list = Arrays.asList("aa", "b", "ccc", "ddd");

        list.sort((s1, s2) -> Integer.compare(s1.length(), s2.length()));
        System.out.println(list);

    }
}