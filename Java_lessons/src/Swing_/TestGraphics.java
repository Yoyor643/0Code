package Swing_;

import javax.swing.*;
import java.awt.*;


public class TestGraphics extends JFrame{

    public TestGraphics() {
        super("这里是界面标题");
        setSize(400, 300); // 默认界面大小
        setVisible(true); //界面可视
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        g.setFont(new Font("SansSerif", Font.BOLD, 12));
        g.setColor(Color.BLUE);
        g.drawString("字体ScansSerif， 粗体，12号， 蓝色", 20,50);

        g.setFont(new Font("Serif", Font.ITALIC, 15));
        g.setColor(Color.RED);
        g.drawString("字体Serif, 斜体， 15号，红色", 250,50);

        g.drawLine(20,0,460,60);

        g.setColor(Color.GREEN);
        g.drawRect(20,70,100,50);
        g.fillRect(130,70,100,50);

        g.setColor(Color.BLACK);

        g.drawArc(50, 60, 50, 50, 50, 120);
    }


    public static void main(String[] args) {
        JFrame.setDefaultLookAndFeelDecorated(true);
        TestGraphics t = new TestGraphics();
        t.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
