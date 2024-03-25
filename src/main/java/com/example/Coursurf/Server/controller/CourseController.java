package com.example.Coursurf.Server.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1")
public class CourseController {
    @GetMapping("/courses")
    public String hello() {
        return "Hello, World!";
    }    
    @GetMapping("/courses/search")
    public String searchCourses() {
        return "Search Courses Endpoint";
    }

}
