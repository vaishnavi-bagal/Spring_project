package com.example.springg;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@SpringBootApplication
public class SpringgApplication {
	@GetMapping("/message")
	public String getMessage() {
		return "Welcome to SpringgApplication";
	}
	public static void main(String[] args) {
		SpringApplication.run(SpringgApplication.class, args);
	}

}
