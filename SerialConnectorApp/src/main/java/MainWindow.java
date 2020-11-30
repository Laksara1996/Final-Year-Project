import javax.swing.*;

public class MainWindow {


    public static void main(String[] args) {
        JFrame frame = new JFrame("Serial Data Transfer App");
        frame.setContentPane(new NewWindow().mainJPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
