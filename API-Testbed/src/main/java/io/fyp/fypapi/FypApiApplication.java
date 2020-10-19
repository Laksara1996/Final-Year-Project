package io.fyp.fypapi;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;

@EnableEurekaClient
@SpringBootApplication
public class FypApiApplication {

	public static void main(String[] args) {
		SpringApplication.run(FypApiApplication.class, args);
	}

}
