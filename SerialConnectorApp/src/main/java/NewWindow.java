import jssc.SerialPortException;
import jssc.SerialPortList;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileNotFoundException;

public class NewWindow extends Component implements DataViwer {
    private JTextField csvFileTextField;
    private JComboBox comboBox1;
    private JComboBox comboBox2;
    private JButton connectButton;
    public JPanel mainJPanel;
    private JButton scanPortsBtn;
    private JTextPane statusTextPlane;
    private JButton openButton;
    private JLabel statusLabel;


    private boolean is_serial_connected = false;
    private SerialPortHandler serialPortHandler;
    private String csvFileLocation = "";

    NewWindow() {
        serialPortHandler = new SerialPortHandler(this);
        String[] serialPortList = SerialPortList.getPortNames();
        int[] boundRates = {115200, 9600, 14400, 19200, 38400, 57600, 115200};
        for (String data : serialPortList) {
            comboBox1.addItem(data);
        }
        for (int data : boundRates) {
            comboBox2.addItem(data);
        }

        scanPortsBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                onScanPortBtnClicked();
            }
        });

        connectButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                onConnectButtonClicked();
            }
        });

        openButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                onOpenButtonClicked();
            }
        });

    }

    private void onOpenButtonClicked() {
        JFileChooser fileChooser = new JFileChooser();
        fileChooser.setCurrentDirectory(new File(System.getProperty("user.home")));
        int result = fileChooser.showOpenDialog(this);
        if (result == JFileChooser.APPROVE_OPTION) {
            File selectedFile = fileChooser.getSelectedFile();
            csvFileLocation = selectedFile.toString();
            csvFileTextField.setText(csvFileLocation);
            statusLabel.setText("CSV File Selected");
            try {
              serialPortHandler.setDataLoader(csvFileLocation);
            } catch (FileNotFoundException e) {
                statusLabel.setText("CSV File Not Found");
                e.printStackTrace();
            }
        }
    }

    private void onScanPortBtnClicked() {
        String[] serialPortList = SerialPortList.getPortNames();
        comboBox1.removeAllItems();
        for (String data : serialPortList) {
            comboBox1.addItem(data);
        }
    }

    private void onConnectButtonClicked() {
        try {
            if (is_serial_connected) {
                // If serial port already connected
                is_serial_connected = false;
                serialPortHandler.disconnect();
                connectButton.setText("Connect");
                statusLabel.setText("Port disconnected");
            } else {
                loadCsvFile();
                serialPortHandler.connect((String) comboBox1.getSelectedItem());
                serialPortHandler.setSerialPartData((int) comboBox2.getSelectedItem());
                connectButton.setText("Disconnect");
                statusLabel.setText("Port Connected");
                is_serial_connected = true;
            }
        } catch (SerialPortException e) {
            statusTextPlane.setText("Error!\n" + e.getMessage());
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            statusTextPlane.setText("Error!\n" + e.getMessage());
            e.printStackTrace();
            statusLabel.setText("Error connecting port");
        }
    }

    private void loadCsvFile() throws FileNotFoundException {
        csvFileLocation = csvFileTextField.getText();
        if (csvFileLocation.equals("")) {
            throw new FileNotFoundException("File Not Selected");
        }
    }

    @Override
    public void appendData(String data) {
        String currentData = statusTextPlane.getText();
        currentData += "\n";
        currentData += data;
        statusTextPlane.setText(currentData);
    }
}
