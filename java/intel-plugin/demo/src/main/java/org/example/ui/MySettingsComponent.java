package org.example.ui;

import com.intellij.openapi.ui.ComboBox;
import com.intellij.ui.components.JBList;
import com.intellij.ui.components.JBPanel;
import com.intellij.ui.components.JBScrollPane;
import com.intellij.ui.treeStructure.Tree;
import com.intellij.util.ui.components.JBComponent;
import org.example.config.MySettings;

import javax.swing.*;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import javax.swing.tree.TreePath;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySettingsComponent {
    private final JPanel panel;
    private final CardLayout cardLayout;
    private final JPanel contentPanel;
    //    private final JTextArea textArea;
//    private final JCheckBox checkBox;

    public MySettingsComponent() {
        panel = new JPanel();
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
        JPanel modelselectionPanel = new ModelSelectionPanel();
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

}
