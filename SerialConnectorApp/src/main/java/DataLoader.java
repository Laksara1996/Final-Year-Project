
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;


public class DataLoader {

    private String csvFile = "/home/sewwandi/Downloads/Final-Year-Project-dev-salaya_Testbed (1)/Final-Year-Project-dev-salaya_Testbed/API-Testbed/src/main/java/io/fyp/fypapi/DataSetSal.csv";
    private String line = "";
    private String cvsSplitBy = ",";

    private ArrayList<Double> time = new ArrayList<Double>();
    private ArrayList<Double> vehicle_speed = new ArrayList<Double>();
    private ArrayList<Double> shift_number = new ArrayList<Double>();
    private ArrayList<Double> engine_load = new ArrayList<Double>();
    private ArrayList<Double> total_acceleration = new ArrayList<Double>();
    private ArrayList<Double> engine_rpm = new ArrayList<Double>();
    private ArrayList<Double> pitch = new ArrayList<Double>();
    private ArrayList<Double> lateral_acceleration = new ArrayList<Double>();
    private ArrayList<Double> passenger_count = new ArrayList<Double>();
    private ArrayList<Double> cars_load = new ArrayList<Double>();
    private ArrayList<Double> air_condition_status = new ArrayList<Double>();
    private ArrayList<Double> window_opening = new ArrayList<Double>();
    private ArrayList<Double> radio_volume = new ArrayList<Double>();
    private ArrayList<Double> rain_intensity = new ArrayList<Double>();
    private ArrayList<Double> visibility = new ArrayList<Double>();
    private ArrayList<Double> drivers_wellbeing = new ArrayList<Double>();
    private ArrayList<Double> driver_rush = new ArrayList<Double>();

    DataLoader(String filepath) throws FileNotFoundException {
        csvFile = filepath;
        BufferedReader br = new BufferedReader(new FileReader(csvFile));

        while (true) {
            try {
                if ((line = br.readLine()) == null) break;
            } catch (IOException e) {
                e.printStackTrace();
            }

            // use comma as separator

            String[] data = line.split(cvsSplitBy);
//	            System.out.println(data[0]);

            time.add(Double.parseDouble(data[0]));
            vehicle_speed.add(Double.parseDouble(data[1]));
            shift_number.add(Double.parseDouble(data[2]));
            engine_load.add(Double.parseDouble(data[3]));
            total_acceleration.add(Double.parseDouble(data[4]));
            engine_rpm.add(Double.parseDouble(data[5]));
            pitch.add(Double.parseDouble(data[6]));
            lateral_acceleration.add(Double.parseDouble(data[7]));
            passenger_count.add(Double.parseDouble(data[8]));
            cars_load.add(Double.parseDouble(data[9]));
            air_condition_status.add(Double.parseDouble(data[10]));
            window_opening.add(Double.parseDouble(data[11]));
            radio_volume.add(Double.parseDouble(data[12]));
            rain_intensity.add(Double.parseDouble(data[13]));
            visibility.add(Double.parseDouble(data[14]));
            drivers_wellbeing.add(Double.parseDouble(data[15]));
            driver_rush.add(Double.parseDouble(data[16]));


        }
    }

    public ArrayList<Double> getData(String id, int count) {

        switch (id) {
            case "time":
                return new ArrayList<Double>(time.subList(count * 10, (count * 10) + 10));
            case "vehicleSpeed":
                return new ArrayList<Double>(vehicle_speed.subList(count * 10, (count * 10) + 10));
            case "shiftNumber":
                return new ArrayList<Double>(shift_number.subList(count * 10, (count * 10) + 10));
            case "engineLoad":
                return new ArrayList<Double>(engine_load.subList(count * 10, (count * 10) + 10));
            case "totalAcceleration":
                return new ArrayList<Double>(total_acceleration.subList(count * 10, (count * 10) + 10));
            case "engineRPM":
                return new ArrayList<Double>(engine_rpm.subList(count * 10, (count * 10) + 10));
            case "pitch":
                return new ArrayList<Double>(pitch.subList(count * 10, (count * 10) + 10));
            case "lateralAcceleration":
                return new ArrayList<Double>(lateral_acceleration.subList(count * 10, (count * 10) + 10));
            case "passengerCount":
                return new ArrayList<Double>(passenger_count.subList(count * 10, (count * 10) + 10));
            case "carLoad":
                return new ArrayList<Double>(cars_load.subList(count * 10, (count * 10) + 10));
            case "airConditionStatus":
                return new ArrayList<Double>(air_condition_status.subList(count * 10, (count * 10) + 10));
            case "windowOpening":
                return new ArrayList<Double>(window_opening.subList(count * 10, (count * 10) + 10));
            case "radioVolume":
                return new ArrayList<Double>(radio_volume.subList(count * 10, (count * 10) + 10));
            case "rainIntensity":
                return new ArrayList<Double>(rain_intensity.subList(count * 10, (count * 10) + 10));
            case "visibility":
                return new ArrayList<Double>(visibility.subList(count * 10, (count * 10) + 10));
            case "driverWellBeing":
                return new ArrayList<Double>(drivers_wellbeing.subList(count * 10, (count * 10) + 10));
            default:
                return new ArrayList<Double>(driver_rush.subList(count * 10, (count * 10) + 10));
        }
    }
}




