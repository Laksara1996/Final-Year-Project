package io.fyp.fypapi.data;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DataController {
	
	@Autowired
	private DataService dataService;
	public int count = -1;
	
	@RequestMapping("/data/{id}")
	public ArrayList<Double> getData(@PathVariable String id) {
		count += 1;
		return dataService.getData(id, count);
	}

}
