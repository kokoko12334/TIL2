package org.example.ui;

import com.intellij.openapi.ui.ComboBox;
import com.intellij.ui.components.JBLabel;
import com.intellij.ui.components.JBPanel;
import com.intellij.ui.components.JBTextField;

import javax.swing.*;
import java.awt.*;
import java.util.*;
import java.util.List;
import java.util.prefs.Preferences;

public class ModelSelectionPanel extends JPanel {

    private final ComboBox<String> companyComboBox;
    private final ComboBox<String> modelComboBox;
    private final JBLabel selectedModelLabel;

    private final JBTextField apiKeyField;

    private static final Map<String, List<String>> COMPANY_MODELS = new LinkedHashMap<>();
    private static final Map<String, String> API_KEYS = new HashMap<>();

    // Preferences를 통한 API 키 저장 (예시)
    private static final Preferences PREFS = Preferences.userNodeForPackage(ModelSelectionPanel.class);
    private static final String API_KEY_PREF = "apiKey";

    static {
        COMPANY_MODELS.put("OpenAI", Arrays.asList("GPT-3.5", "GPT-4.0"));
        COMPANY_MODELS.put("Google", Arrays.asList("Gemini Pro", "Gemini Ultra"));
        COMPANY_MODELS.put("Anthropic", Arrays.asList("Claude 2", "Claude 3"));
        COMPANY_MODELS.put("Meta", Arrays.asList("Llama 3", "Llama 2"));
        COMPANY_MODELS.put("Mistral", Arrays.asList("Mistral 7B", "Mixtral"));
        COMPANY_MODELS.put("로컬 모델", Arrays.asList("LLM Local", "Custom Model"));

        API_KEYS.put("OpenAI", "");
        API_KEYS.put("Google", "");
        API_KEYS.put("Anthropic", "");
        API_KEYS.put("Meta", "");
        API_KEYS.put("Mistral", "");
        API_KEYS.put("로컬 모델", "");
    }

    public ModelSelectionPanel() {
        setLayout(new BorderLayout());

        // 선택된 모델을 표시하는 Label
        selectedModelLabel = new JBLabel("Selected Model: ");

        // 회사 선택 드롭다운
        companyComboBox = new ComboBox<>(COMPANY_MODELS.keySet().toArray(new String[0]));
        companyComboBox.addActionListener(e -> updateModelComboBox());

        // API 키 입력 필드
        apiKeyField = new JBTextField(20);
        // 저장된 API 키가 있으면 불러오기
        String savedApiKey = PREFS.get(API_KEY_PREF, "");
        apiKeyField.setText(savedApiKey);

        // 모델 선택 드롭다운 (초기값 설정)
        modelComboBox = new ComboBox<>();
        updateModelComboBox(); // 초기 모델 목록 설정

        // API 키 저장 버튼
        JButton saveApiKeyButton = new JButton("Save API Key");
        saveApiKeyButton.addActionListener(e -> {
            String apiKey = apiKeyField.getText();
            // Preferences에 저장 (실제 사용 시엔 보안 저장 방법 고려)
            PREFS.put(API_KEY_PREF, apiKey);
            // 저장 후 라벨 업데이트 (예시)
            selectedModelLabel.setText("Selected Model: " + modelComboBox.getSelectedItem() + " | API Key saved.");
        });

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
