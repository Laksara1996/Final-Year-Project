package io.fyp.microservices.accontrol.model;

public class AcControl {
    private Double passenger_count;
    private Double air_condition_status;
    private Double window_opening;

    public AcControl() {
    }



    public AcControl(Double passenger_count, Double air_condition_status, Double window_opening) {
        this.passenger_count = passenger_count;
        this.air_condition_status = air_condition_status;
        this.window_opening = window_opening;
    }

    public Double getPassenger_count() {
        return passenger_count;
    }

    public void setPassenger_count(Double passenger_count) {
        this.passenger_count = passenger_count;
    }

    public Double getAir_condition_status() {
        return air_condition_status;
    }

    public void setAir_condition_status(Double air_condition_status) {
        this.air_condition_status = air_condition_status;
    }

    public Double getWindow_opening() {
        return window_opening;
    }

    public void setWindow_opening(Double window_opening) {
        this.window_opening = window_opening;
    }


}
