package io.fyp.microservices.accontrol.resources;

import io.fyp.microservices.accontrol.model.AcControl;
import io.fyp.microservices.accontrol.model.AirCondition;
import io.fyp.microservices.accontrol.model.PassengerCount;
import io.fyp.microservices.accontrol.model.WindowOpening;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.sql.SQLOutput;

@RestController
@RequestMapping("/acdata")
public class AcControlResource {

    public void getAirCondition(){
        final String uri = "http://localhost:5000/data/air_condition_status";
        RestTemplate restTemplate =new RestTemplate();
        AirCondition result = restTemplate.getForObject(uri,AirCondition.class);
       // System.out.println(result);
    }

    public void getPassengerCount(){
        final String uri = "http://localhost:5000/data/passenger_count";
        RestTemplate restTemplate =new RestTemplate();
        PassengerCount result = restTemplate.getForObject(uri,PassengerCount.class);
        HttpHeaders result2 = restTemplate.headForHeaders(uri);
     //   System.out.println(result);
    }

    public void getWindowOpening(){
        final String uri = "http://localhost:5000/data/window_opening";
        RestTemplate restTemplate =new RestTemplate();
        WindowOpening result = restTemplate.getForObject(uri,WindowOpening.class);
      //  System.out.println(result);
    }



//    @Autowired
//    private RestTemplate restTemplate;
//
//
//    public Double getAcInfo(){
//
//        ResponseEntity<AcControl> acControl = restTemplate.getForEntity("localhost:5000/data/air_condition_status/" , AcControl.class);
//                //("localhost:5000/data/" + acId + AcControl.class);
//
//        return AcControl.getAir_condition_status();
//
//    }



}
