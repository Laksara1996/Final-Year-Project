package io.fyp.fypapi.data;

import java.util.ArrayList;


public class Data {

	private ArrayList<Double> time;;
	private ArrayList<Double> vehicle_speed;
	private ArrayList<Double> shift_number;
	private ArrayList<Double> engine_load;
	private ArrayList<Double> total_acceleration;
	private ArrayList<Double> engine_rpm;
	private ArrayList<Double> pitch;
	private ArrayList<Double> lateral_acceleration;
	private ArrayList<Double> passenger_count;
	private ArrayList<Double> cars_load;
	private ArrayList<Double> air_condition_status;
	private ArrayList<Double> window_opening;
	private ArrayList<Double> radio_volume;
	private ArrayList<Double> rain_intensity;
	private ArrayList<Double> visibility;
	private ArrayList<Double> drivers_wellbeing;
	private ArrayList<Double> driver_rush;
	
	
	public Data(ArrayList<Double> time, ArrayList<Double> vehicle_speed, ArrayList<Double> shift_number,
			ArrayList<Double> engine_load, ArrayList<Double> total_acceleration, ArrayList<Double> engine_rpm,
			ArrayList<Double> pitch, ArrayList<Double> lateral_acceleration, ArrayList<Double> passenger_count,
			ArrayList<Double> cars_load, ArrayList<Double> air_condition_status, ArrayList<Double> window_opening,
			ArrayList<Double> radio_volume, ArrayList<Double> rain_intensity, ArrayList<Double> visibility,
			ArrayList<Double> drivers_wellbeing, ArrayList<Double> driver_rush) {
		super();
		this.time = time;
		this.vehicle_speed = vehicle_speed;
		this.shift_number = shift_number;
		this.engine_load = engine_load;
		this.total_acceleration = total_acceleration;
		this.engine_rpm = engine_rpm;
		this.pitch = pitch;
		this.lateral_acceleration = lateral_acceleration;
		this.passenger_count = passenger_count;
		this.cars_load = cars_load;
		this.air_condition_status = air_condition_status;
		this.window_opening = window_opening;
		this.radio_volume = radio_volume;
		this.rain_intensity = rain_intensity;
		this.visibility = visibility;
		this.drivers_wellbeing = drivers_wellbeing;
		this.driver_rush = driver_rush;
	}

	
	public ArrayList<Double> getTime() {
		return time;
	}

	public void setTime(ArrayList<Double> time) {
		this.time = time;
	}

	public ArrayList<Double> getVehicle_speed() {
		return vehicle_speed;
	}

	public void setVehicle_speed(ArrayList<Double> vehicle_speed) {
		this.vehicle_speed = vehicle_speed;
	}

	public ArrayList<Double> getShift_number() {
		return shift_number;
	}

	public void setShift_number(ArrayList<Double> shift_number) {
		this.shift_number = shift_number;
	}

	public ArrayList<Double> getEngine_load() {
		return engine_load;
	}

	public void setEngine_load(ArrayList<Double> engine_load) {
		this.engine_load = engine_load;
	}

	public ArrayList<Double> getTotal_acceleration() {
		return total_acceleration;
	}

	public void setTotal_acceleration(ArrayList<Double> total_acceleration) {
		this.total_acceleration = total_acceleration;
	}

	public ArrayList<Double> getEngine_rpm() {
		return engine_rpm;
	}

	public void setEngine_rpm(ArrayList<Double> engine_rpm) {
		this.engine_rpm = engine_rpm;
	}

	public ArrayList<Double> getPitch() {
		return pitch;
	}

	public void setPitch(ArrayList<Double> pitch) {
		this.pitch = pitch;
	}

	public ArrayList<Double> getLateral_acceleration() {
		return lateral_acceleration;
	}

	public void setLateral_acceleration(ArrayList<Double> lateral_acceleration) {
		this.lateral_acceleration = lateral_acceleration;
	}

	public ArrayList<Double> getPassenger_count() {
		return passenger_count;
	}

	public void setPassenger_count(ArrayList<Double> passenger_count) {
		this.passenger_count = passenger_count;
	}

	public ArrayList<Double> getCars_load() {
		return cars_load;
	}

	public void setCars_load(ArrayList<Double> cars_load) {
		this.cars_load = cars_load;
	}

	public ArrayList<Double> getAir_condition_status() {
		return air_condition_status;
	}

	public void setAir_condition_status(ArrayList<Double> air_condition_status) {
		this.air_condition_status = air_condition_status;
	}

	public ArrayList<Double> getWindow_opening() {
		return window_opening;
	}

	public void setWindow_opening(ArrayList<Double> window_opening) {
		this.window_opening = window_opening;
	}

	public ArrayList<Double> getRadio_volume() {
		return radio_volume;
	}

	public void setRadio_volume(ArrayList<Double> radio_volume) {
		this.radio_volume = radio_volume;
	}

	public ArrayList<Double> getRain_intensity() {
		return rain_intensity;
	}

	public void setRain_intensity(ArrayList<Double> rain_intensity) {
		this.rain_intensity = rain_intensity;
	}

	public ArrayList<Double> getVisibility() {
		return visibility;
	}

	public void setVisibility(ArrayList<Double> visibility) {
		this.visibility = visibility;
	}

	public ArrayList<Double> getDrivers_wellbeing() {
		return drivers_wellbeing;
	}

	public void setDrivers_wellbeing(ArrayList<Double> drivers_wellbeing) {
		this.drivers_wellbeing = drivers_wellbeing;
	}

	public ArrayList<Double> getDriver_rush() {
		return driver_rush;
	}

	public void setDriver_rush(ArrayList<Double> driver_rush) {
		this.driver_rush = driver_rush;
	}

	public Data() {

	}
	
}
