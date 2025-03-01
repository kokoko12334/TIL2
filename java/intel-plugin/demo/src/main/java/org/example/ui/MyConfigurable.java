package org.example.ui;

import com.intellij.openapi.options.Configurable;
import org.example.config.MySettings;
import org.jetbrains.annotations.Nullable;

import javax.swing.*;

public class MyConfigurable implements Configurable {
    private MySettingsComponent mySettingsComponent;

    @Override
    public String getDisplayName() {
        return "My Plugin Settings";
    }

    @Nullable
    @Override
    public JComponent createComponent() {
        mySettingsComponent = new MySettingsComponent();
        System.out.println("createComponent");
        return mySettingsComponent.getPanel();
    }

    @Override
    public boolean isModified() {
        MySettings settings = MySettings.getInstance();
        String selectedOption = mySettingsComponent.getSelectedOption();
        System.out.println("isModified");
        return !selectedOption.equals(settings.getState().theme);
    }


    @Override
    public void apply() {
        MySettings settings = MySettings.getInstance();
        settings.setTheme(mySettingsComponent.getSelectedOption());
        System.out.println("apply");
    }

    @Override
    public void reset() {
        MySettings settings = MySettings.getInstance();
        mySettingsComponent.setSelectedOption(settings.getTheme());
        System.out.println("reset");
    }
}
