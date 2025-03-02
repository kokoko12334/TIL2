package org.example.ui;

import com.intellij.openapi.ui.ComboBox;
import com.intellij.ui.components.JBLabel;
import com.intellij.ui.components.JBPanel;

import javax.swing.*;
import java.awt.*;
import java.util.*;
import java.util.List;

public class ModelSelectionPanel extends JBPanel {

    private ComboBox<String> companyComboBox;
    private ComboBox<String> modelComboBox;
    private JBLabel selectedModelLabel;

    private static final Map<String, List<String>> COMPANY_MODELS = new HashMap<>();

    static {
        COMPANY_MODELS.put("OpenAI", Arrays.asList("GPT-3.5", "GPT-4.0"));
        COMPANY_MODELS.put("Google", Arrays.asList("Gemini Pro", "Gemini Ultra"));
        COMPANY_MODELS.put("Anthropic", Arrays.asList("Claude 2", "Claude 3"));
        COMPANY_MODELS.put("Meta", Arrays.asList("Llama 3", "Llama 2"));
        COMPANY_MODELS.put("Mistral", Arrays.asList("Mistral 7B", "Mixtral"));
        COMPANY_MODELS.put("로컬 모델", Arrays.asList("LLM Local", "Custom Model"));
    }

    public ModelSelectionPanel() {
        setLayout(new BorderLayout());

        // 회사 선택 드롭다운
        companyComboBox = new ComboBox<>(COMPANY_MODELS.keySet().toArray(new String[0]));
        companyComboBox.addActionListener(e -> updateModelComboBox());

        // 모델 선택 드롭다운 (초기값 설정)
        modelComboBox = new ComboBox<>();
        updateModelComboBox(); // 초기 모델 목록 설정

        // 선택된 모델을 표시하는 Label
        selectedModelLabel = new JBLabel("Selected Model");

        // 모델 선택 이벤트 리스너
        modelComboBox.addActionListener(e -> updateSelectedModel());

        // 상단 패널 (회사 선택)
        JPanel topPanel = new JBPanel<>();
        topPanel.add(new JBLabel("Select Company:"));
        topPanel.add(companyComboBox);

        // 중앙 패널 (모델 선택)
        JPanel centerPanel = new JPanel();
        centerPanel.add(new JLabel("Select Model:"));
        centerPanel.add(modelComboBox);

        // 패널 구성
        add(topPanel, BorderLayout.NORTH);
        add(centerPanel, BorderLayout.CENTER);
        add(selectedModelLabel, BorderLayout.SOUTH);
    }

    // 회사 선택 시 모델 목록 업데이트
    private void updateModelComboBox() {
        String selectedCompany = (String) companyComboBox.getSelectedItem();
        List<String> models = COMPANY_MODELS.getOrDefault(selectedCompany, Collections.emptyList());

        // 모델 목록 업데이트
        modelComboBox.removeAllItems();
        for (String model : models) {
            modelComboBox.addItem(model);
        }

        updateSelectedModel(); // 모델 변경 시 선택된 값도 업데이트
    }

    // 선택된 모델을 UI에 반영
    private void updateSelectedModel() {
        String selectedModel = (String) modelComboBox.getSelectedItem();
        selectedModelLabel.setText("Selected Model: " + (selectedModel != null ? selectedModel : "no"));
    }

}
