package Swing_;

import java.awt.event.*;
import javax.swing.*;

public class ImplementMouseListener implements MouseListener {

    JFrame f;

    public ImplementMouseListener() {
        f = new JFrame();              // 创建窗口
        f.setSize(300, 150);           // 设置窗口大小
        f.setVisible(true);            // 显示窗口
        f.addMouseListener(this);      // 给窗口添加鼠标监听器
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public void mousePressed(MouseEvent e) {
        ;// 鼠标按下
    }

    public void mouseReleased(MouseEvent e) {
        ;// 鼠标释放
    }

    public void mouseEntered(MouseEvent e) {
        ;// 鼠标进入窗口
    }

    public void mouseExited(MouseEvent e) {
        ;// 鼠标离开窗口
    }

    public void mouseClicked(MouseEvent e) {
        // 鼠标点击
        f.setTitle("点击坐标为 (" + e.getX() + ", " + e.getY() + ")");
    }

    public static void main(String[] args) {
        new ImplementMouseListener();
    }
}
