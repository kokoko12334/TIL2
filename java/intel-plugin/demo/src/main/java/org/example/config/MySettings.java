package org.example.config;

import com.intellij.openapi.components.*;
import com.intellij.openapi.components.State;
import org.jetbrains.annotations.NotNull;

@Service
@State(
        name = "org.example.config.MySettings",
        storages = @Storage("MySettings.xml")
)
public final class MySettings implements PersistentStateComponent<MySettings.State> {

    // ✅ 내부 State 클래스 정의 (저장될 데이터)
    public static class State {
        public String theme = "Light";
    }

    private State myState = new State();  // 초기 상태값

    @Override
    public State getState() {
        return myState;
    }

    @Override
    public void loadState(@NotNull State state) {
        this.myState = state;
    }

    public static MySettings getInstance() {
        return ServiceManager.getService(MySettings.class);
    }

    public String getTheme() {
        return myState.theme;
    }

    public void setTheme(String theme) {
        myState.theme = theme;
    }
}
