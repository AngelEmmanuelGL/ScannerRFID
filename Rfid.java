
import javax.swing.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class Rfid{

    public static void main(String[] args) {
        JFrame frame = new JFrame("Lector RFID");
        JTextArea textArea = new JTextArea();

        textArea.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
                // Captura cada carácter ingresado
                System.out.print(e.getKeyChar());
            }

            @Override
            public void keyPressed(KeyEvent e) {
                // No hace nada aquí
            }

            @Override
            public void keyReleased(KeyEvent e) {
                // No hace nada aquí
            }
        });

        frame.add(textArea);
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
