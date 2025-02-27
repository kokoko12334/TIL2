package org.example.demo1.services;

import com.intellij.openapi.components.Service;
import com.intellij.openapi.project.Project;

@Service
public class MyProjectService {
    private final Project project;

    public MyProjectService(Project project) {
        this.project = project;
    }

    public String getProjectName() {
        return project.getName();
    }

    public void doSomething() {
        System.out.println("do something");
    }

}
