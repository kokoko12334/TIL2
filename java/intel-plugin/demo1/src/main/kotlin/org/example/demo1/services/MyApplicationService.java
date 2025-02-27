package org.example.demo1.services;

import com.intellij.openapi.components.Service;

@Service
public final class MyApplicationService {
    public MyApplicationService() {
    }

    public void globalOperation() {
        System.out.println("globally");
    }
}
