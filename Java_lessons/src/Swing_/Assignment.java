package Swing_;

import javax.swing.*;
import java.awt.*;

public class Assignment extends JFrame {

    private DefaultListModel<String> listModel;
    private JList<String> taskList;
    private JTextField inputField;

    public Assignment() {
        setTitle("待办事项清单");
        setSize(400, 300);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        listModel = new DefaultListModel<>();
        taskList = new JList<>(listModel);
        inputField = new JTextField();

        JButton addButton = new JButton("新增");
        JButton deleteButton = new JButton("删除");
        JButton clearButton = new JButton("清空");

        JPanel topPanel = new JPanel(new BorderLayout());
        topPanel.add(inputField, BorderLayout.CENTER);
        topPanel.add(addButton, BorderLayout.EAST);

        JPanel bottomPanel = new JPanel();
        bottomPanel.add(deleteButton);
        bottomPanel.add(clearButton);

        add(topPanel, BorderLayout.NORTH);
        add(new JScrollPane(taskList), BorderLayout.CENTER);
        add(bottomPanel, BorderLayout.SOUTH);

        addButton.addActionListener(e -> addTask());
        deleteButton.addActionListener(e -> deleteTask());
        clearButton.addActionListener(e -> clearTasks());

        inputField.addActionListener(e -> addTask());
    }

    private void addTask() {
        String text = inputField.getText().trim();

        if (text.isEmpty()) {
            JOptionPane.showMessageDialog(this, "请输入待办事项");
            return;
        }

        listModel.addElement(text);
        inputField.setText("");
    }

    private void deleteTask() {
        int index = taskList.getSelectedIndex();

        if (index == -1) {
            JOptionPane.showMessageDialog(this, "请先选择要删除的事项");
            return;
        }

        listModel.remove(index);
    }

    private void clearTasks() {
        listModel.clear();
    }

    public static void main(String[] args) {
        new Assignment().setVisible(true);
    }
}
