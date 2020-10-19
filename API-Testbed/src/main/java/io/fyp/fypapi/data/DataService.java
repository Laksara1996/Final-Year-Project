package io.fyp.fypapi.data;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

import org.springframework.stereotype.Service;


@Service
public class DataService {

	private String csvFile = "F:\\ACADEMIC\\Semester 7\\CO 421 CO 425 Final Year Project\\Project\\fyp-dataset-api\\API-Testbed\\src\\main\\java\\io\\fyp\\fypapi\\DataSetSal.csv";
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

    {
	    try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
	
	        while ((line = br.readLine()) != null) {
	
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
	
	    } catch (IOException e) {
	        e.printStackTrace();
	    }
    }

	
    public ArrayList<Double> getData(String id) {
		switch(id) {
			case "time":
				return time;
			case "vehicleSpeed":
				return vehicle_speed;
			case "shiftNumber":
				return shift_number;
			case "engineLoad":
				return engine_load;
			case "totalAcceleration":
				return total_acceleration;
			case "engineRPM":
				return engine_rpm;
			case "pitch":
				return pitch;
			case "lateralAcceleration":
				return lateral_acceleration;
			case "passengerCount":
				return passenger_count;
			case "carLoad":
				return cars_load;
			case "airConditionStatus":
				return air_condition_status;
			case "windowOpening":
				return window_opening;
			case "radioVolume":
				return radio_volume;
			case "rainIntensity":
				return rain_intensity;
			case "visibility":
				return visibility;
			case "DriverWellBeing":
				return drivers_wellbeing;
			default:
				return driver_rush;
		}
	}
}

