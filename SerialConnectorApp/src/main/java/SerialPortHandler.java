import jssc.SerialPort;
import jssc.SerialPortException;
import jssc.SerialPortTimeoutException;

import java.io.FileNotFoundException;
import java.util.Random;
import java.util.concurrent.*;

public class SerialPortHandler {

    private DataLoader dataLoader;
    private int timeCount = -1;
    private int vehicleSpeedCount = -1;
    private int shiftNumberCount = -1;
    private int engineLoadCount = -1;
    private int totalAccelerationCount = -1;
    private int engineRPMCount = -1;
    private int pitchCount = -1;
    private int lateralAccelerationCount = -1;
    private int passengerCountCount = -1;
    private int carLoadCount = -1;
    private int airConditionStatusCount = -1;
    private int windowOpeningCount = -1;
    private int radioVolumeCount = -1;
    private int rainIntensityCount = -1;
    private int visibilityCount = -1;
    private int driverWellBeingCount = -1;
    private int driverRushCount = -1;

    DataViwer dataViwer;
    SerialPort serialPort;
    ScheduledExecutorService executorService = Executors.newScheduledThreadPool(1);

    SerialPortHandler(DataViwer dataViwer) {
        this.dataViwer = dataViwer;
    }

    public void setDataLoader(String filepath) throws FileNotFoundException {
        dataLoader = new DataLoader(filepath);
    }

    public void setSerialPartData(int boundRate) throws SerialPortException {
        serialPort.setParams(boundRate, SerialPort.DATABITS_8, SerialPort.STOPBITS_1, SerialPort.PARITY_NONE);
    }

    public void connect(String portName) throws SerialPortException {
        serialPort = new SerialPort(portName);
        serialPort.openPort();
        executorService.scheduleWithFixedDelay(new Runnable() {
                                                   public void run() {
                                                       String data = null;
                                                       try {
                                                           data = serialPort.readString();
                                                       } catch (SerialPortException e) {
                                                           e.printStackTrace();
                                                       }
                                                       if (data != null) {
                                                           System.out.println(data);
                                                           processData(data);
                                                       }
                                                   }
                                               },
                100, 100,
                TimeUnit.MILLISECONDS);
    }


    public void disconnect() throws SerialPortException {
        executorService.shutdown();
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        if (!executorService.isShutdown()) {
            executorService.shutdownNow();
        }
        if (serialPort.isOpened()) {
            serialPort.closePort();
            serialPort = null;
        }
    }

    private void processData(String data) {

        // If GT is got, send some data
        dataViwer.appendData("Recieved : " + data);
        if (data.contains("#A")) {
            timeCount++;
            String timeData = String.valueOf(dataLoader.getData("time",timeCount));

            String writeData = "time," + timeData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#B")) {
            vehicleSpeedCount++;
            String csvData = String.valueOf(dataLoader.getData("vehicleSpeed",vehicleSpeedCount));

            String writeData = "vehicleSpeed," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#C")) {
            shiftNumberCount++;
            String csvData = String.valueOf(dataLoader.getData("shiftNumber",shiftNumberCount));

            String writeData = "shiftNumber," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#D")) {
            engineLoadCount++;
            String csvData = String.valueOf(dataLoader.getData("engineLoad",engineLoadCount));

            String writeData = "engineLoad," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#E")) {
            totalAccelerationCount++;
            String csvData = String.valueOf(dataLoader.getData("totalAcceleration",totalAccelerationCount));

            String writeData = "totalAcceleration," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#F")) {
            engineRPMCount++;
            String csvData = String.valueOf(dataLoader.getData("engineRPM",engineRPMCount));

            String writeData = "engineRPM," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#G")) {
            pitchCount++;
            String csvData = String.valueOf(dataLoader.getData("pitch",pitchCount));

            String writeData = "pitch," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#H")) {
            lateralAccelerationCount++;
            String csvData = String.valueOf(dataLoader.getData("lateralAcceleration",lateralAccelerationCount));

            String writeData = "lateralAcceleration," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#I")) {
            passengerCountCount++;
            String csvData = String.valueOf(dataLoader.getData("passengerCount",passengerCountCount));

            String writeData = "passengerCount," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#J")) {
            carLoadCount++;
            String csvData = String.valueOf(dataLoader.getData("carLoad",carLoadCount));

            String writeData = "carLoad," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#K")) {
            airConditionStatusCount++;
            String csvData = String.valueOf(dataLoader.getData("airConditionStatus",airConditionStatusCount));

            String writeData = "airConditionStatus," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#L")) {
            windowOpeningCount++;
            String csvData = String.valueOf(dataLoader.getData("windowOpening",windowOpeningCount));

            String writeData = "windowOpening," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#M")) {
            radioVolumeCount++;
            String csvData = String.valueOf(dataLoader.getData("radioVolume",radioVolumeCount));

            String writeData = "radioVolume," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#N")) {
            rainIntensityCount++;
            String csvData = String.valueOf(dataLoader.getData("rainIntensity",rainIntensityCount));

            String writeData = "rainIntensity," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#O")) {
            visibilityCount++;
            String csvData = String.valueOf(dataLoader.getData("visibility",visibilityCount));

            String writeData = "visibility," + csvData + "\n";
            writeSerialData(writeData);


        }else if (data.contains("#P")) {
            driverWellBeingCount++;
            String csvData = String.valueOf(dataLoader.getData("driverWellBeing",driverWellBeingCount));

            String writeData = "driverWellBeing," + csvData + "\n";
            writeSerialData(writeData);


        } else if (data.contains("#Q")) {
            driverRushCount++;
            String csvData = String.valueOf(dataLoader.getData("",driverRushCount));

            String writeData = "driverRush" + csvData + "\n";
            writeSerialData(writeData);
        }

    }

    private void writeSerialData(String data) {
        try {
            serialPort.writeString(data);
            dataViwer.appendData("Send : " + data);
        } catch (SerialPortException e) {
            e.printStackTrace();
        }
    }


}
