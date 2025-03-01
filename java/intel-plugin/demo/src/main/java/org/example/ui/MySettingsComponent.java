package org.example.ui;

import com.intellij.openapi.ui.ComboBox;
import com.intellij.ui.components.JBList;
import org.example.config.MySettings;

import javax.swing.*;
import java.awt.*;

public class MySettingsComponent {
    private final JPanel panel;
    private final ComboBox<String> comboBox;
    private final JTextArea textArea;
    private final JCheckBox checkBox;

    public MySettingsComponent() {
        panel = new JPanel(new BorderLayout());
        String[] options = {"Option 1", "Option 2", "Option 3"};
        comboBox = new ComboBox<>(options);
        panel.add(new JLabel("Select an option:"), BorderLayout.CENTER);
        panel.add(comboBox, BorderLayout.CENTER);
        panel.add(new JLabel("상단 패널"), BorderLayout.NORTH);
        panel.add(new JButton("왼쪽 버튼"), BorderLayout.WEST);
        panel.add(new JButton("오른쪽 버튼"), BorderLayout.EAST);
        panel.add(new JTextArea(5, 20), BorderLayout.CENTER);
        panel.add(new JButton("하단 버튼"), BorderLayout.SOUTH);

        // 좌측 메뉴처럼 패널 추가 (예시)
        JPanel leftPanel = new JPanel();
        leftPanel.setLayout(new BoxLayout(leftPanel, BoxLayout.Y_AXIS));
        leftPanel.add(new JButton("커밋 메시지 생성"));
        leftPanel.add(new JButton("문서 작성"));
        leftPanel.add(new JButton("유닛 테스트 생성"));

        // 우측 패널: 설명 텍스트 영역
        JPanel rightPanel = new JPanel(new BorderLayout());
        textArea = new JTextArea(10, 40);
        checkBox = new JCheckBox("옵션 활성화");

        rightPanel.add(new JLabel("설정 설명"), BorderLayout.NORTH);
        rightPanel.add(new JScrollPane(textArea), BorderLayout.CENTER);
        rightPanel.add(checkBox, BorderLayout.SOUTH);
        String[] items = {"Item 1", "Item 2", "Item 3"};
        JList<String> list = new JBList<>(items);
        list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        // 전체 레이아웃
        panel.add(leftPanel, BorderLayout.WEST);
        panel.add(rightPanel, BorderLayout.CENTER);
        panel.add(list, BorderLayout.EAST);


    }

    public JPanel getPanel() {
        return panel;
    }

    public String getSelectedOption() {
        return (String) comboBox.getSelectedItem();
    }

    public void setSelectedOption(String option) {
        comboBox.setSelectedItem(option);
    }
}
