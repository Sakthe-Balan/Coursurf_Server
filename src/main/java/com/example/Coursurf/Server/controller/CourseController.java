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

    @GetMapping("/courses/semantic_search")
    public String semanticSearchCourses() {
        return "Semantic Search Courses Endpoint";
    }

    @GetMapping("/courses/filter")
    public String filterCourse() {
        return "Filter Course Endpoint";
    }

    @GetMapping("/courses/view")
    public String viewCourse() {
        return "View Course Endpoint";
    }

}
