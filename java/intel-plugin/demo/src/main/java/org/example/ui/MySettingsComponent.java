package org.example.ui;

import com.intellij.openapi.ui.ComboBox;
import com.intellij.ui.components.JBList;
import com.intellij.ui.components.JBPanel;
import com.intellij.ui.components.JBScrollPane;
import com.intellij.ui.treeStructure.Tree;
import org.example.config.MySettings;

import javax.swing.*;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import javax.swing.tree.TreePath;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySettingsComponent {
    private final JBPanel panel;
    private final ComboBox<String> comboBox;
    private final CardLayout cardLayout;
    private final JBPanel contentPanel;
    private final JBPanel modelselectionPanel = new ModelSelectionPanel();
//    private final JTextArea textArea;
//    private final JCheckBox checkBox;

    public MySettingsComponent() {
        panel = new JBPanel<>();
        String[] options = {"Option 1", "Option 2", "Option 3"};
        comboBox = new ComboBox<>(options);
//        panel.add(new JLabel("Select an option:"), BorderLayout.CENTER);
//        panel.add(comboBox, BorderLayout.CENTER);
//        panel.add(new JLabel("상단 패널"), BorderLayout.NORTH);
//        panel.add(new JButton("왼쪽 버튼"), BorderLayout.WEST);
//        panel.add(new JButton("오른쪽 버튼"), BorderLayout.EAST);
//        panel.add(new JTextArea(5, 20), BorderLayout.CENTER);
//        panel.add(new JButton("하단 버튼"), BorderLayout.SOUTH);
//
//        // 좌측 메뉴처럼 패널 추가 (예시)
//        JPanel leftPanel = new JPanel();
//        leftPanel.setLayout(new BoxLayout(leftPanel, BoxLayout.Y_AXIS));
//        leftPanel.add(new JButton("커밋 메시지 생성"));
//        leftPanel.add(new JButton("문서 작성"));
//        leftPanel.add(new JButton("유닛 테스트 생성"));
//
//        // 우측 패널: 설명 텍스트 영역
//        JPanel rightPanel = new JPanel(new BorderLayout());
//        textArea = new JTextArea(10, 40);
//        checkBox = new JCheckBox("옵션 활성화");
//
//        rightPanel.add(new JLabel("설정 설명"), BorderLayout.NORTH);
//        rightPanel.add(new JScrollPane(textArea), BorderLayout.CENTER);
//        rightPanel.add(checkBox, BorderLayout.SOUTH);
//        String[] items = {"Item 1", "Item 2", "Item 3"};
//        JList<String> list = new JBList<>(items);
//        list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
//        // 전체 레이아웃
//        panel.add(leftPanel, BorderLayout.WEST);
//        panel.add(rightPanel, BorderLayout.CENTER);
//        panel.add(list, BorderLayout.EAST);


        // 패널 생성 및 GridLayout 설정 (2행 2열)
//        panel = new JPanel(new GridLayout(2, 2, 10, 10)); // 행, 열, 수평 간격, 수직 간격
//        // 버튼 추가
//        panel.add(new JButton("Button 1"));
//        panel.add(new JButton("Button 2"));
//        panel.add(new JButton("Button 3"));
//        panel.add(new JButton("Button 4"));


        panel.setLayout(new BorderLayout());

        // 좌측 네비게이션 패널 (JTree)
        DefaultMutableTreeNode root = new DefaultMutableTreeNode("설정");
        DefaultMutableTreeNode category1 = new DefaultMutableTreeNode("Model");
        category1.add(new DefaultMutableTreeNode("Model Selection"));

        DefaultMutableTreeNode category2 = new DefaultMutableTreeNode("문서 작성");
        category2.add(new DefaultMutableTreeNode("Python"));
        category2.add(new DefaultMutableTreeNode("Java"));
        category2.add(new DefaultMutableTreeNode("Kotlin"));

        root.add(category1);
        root.add(category2);

        JTree tree = new Tree(new DefaultTreeModel(root));
        tree.setRootVisible(false);
        JScrollPane treeScrollPane = new JBScrollPane(tree);

        // 우측 패널 (CardLayout)
        cardLayout = new CardLayout();
        contentPanel = new JBPanel<>(cardLayout);

        // 각 패널 추가
        contentPanel.add(modelselectionPanel, "Model Selection");
        contentPanel.add(new JLabel("Python 문서 작성 설정 화면"), "Python");
        contentPanel.add(new JLabel("Java 문서 작성 설정 화면"), "Java");
        contentPanel.add(new JLabel("Kotlin 문서 작성 설정 화면"), "Kotlin");

        // JTree 클릭 이벤트 (선택한 메뉴에 따라 카드 변경)
        tree.addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                TreePath path = tree.getPathForLocation(e.getX(), e.getY());
                if (path != null) {
                    String selectedNode = path.getLastPathComponent().toString();
                    cardLayout.show(contentPanel, selectedNode);
                }
            }
        });

        // 좌우 패널을 나누는 JSplitPane
        JSplitPane splitPane = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, treeScrollPane, contentPanel);
        splitPane.setDividerLocation(200);

        panel.add(splitPane, BorderLayout.CENTER);
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
